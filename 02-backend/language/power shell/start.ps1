<#
.SYNOPSIS
    拉起被测集群。

.DESCRIPTION
    这里的集群分两种模式，一种是 bundle 模式，一种是 separation 模式。覆盖版本有 main 和 LTS/2.3 两种。默认是 main latest bundle。

.PARAMETER 参数名
    -b：分支名，main 或 LTS/2.3，默认是 main。
    -t：tag 名，latest 或者具体的 tag 名，默认是 latest。
    -M：模式，bundle 或 separation，默认是 bundle。
    这是示例脚本的参数说明。

.EXAMPLE
    示例用法1：
    .\start.ps1 -b main -t latest -M bundle

.EXAMPLE
    示例用法2：
    .\start.ps1 -b main -t latest -M separation
#>
param (
    [Parameter(Mandatory=$true)]
    [string]$b = "main",
    [string]$t = "latest",
    [string]$M = "bundle"
)
$ErrorActionPreference = "Stop"
$workingDir = "C:\Users\cnosdb\Documents\code\cnosdb"
$dataDir = "c:\tmp\"
Set-Location $workingDir

function Clean-Environment {
    Write-Host "clean environment..."
    Remove-Item -Path "$dataDir\*" -Recurse -Force -ErrorAction SilentlyContinue
    # & cargo clean
    Get-Process | Where-Object { $_.ProcessName -like "*cnsodb*" } | Stop-Process -Force
    Write-Host "clean environment done"
}

function Build {
    Write-Host "build..."
    # & cargo build --release --workspace --bins
    Write-Host "build done"

}

function Meta {
    Write-Host "meta..."
    Write-Host "Start 3 uninitialized cnosdb-meta servers..."
    Write-Host "start meta"
    Start-Process -FilePath "$workingDir/target/release/cnosdb-meta.exe" -ArgumentList "--config", "$workingDir/meta/config/config_8901.toml" -NoNewWindow
    Write-Host "Server 1 started"
    Start-Sleep -Seconds 2
    Start-Process -FilePath "$workingDir/target/release/cnosdb-meta.exe" -ArgumentList "--config", "$workingDir/meta/config/config_8911.toml" -NoNewWindow
    Write-Host "Server 2 started"
    Start-Sleep -Seconds 2
    Start-Process -FilePath "$workingDir/target/release/cnosdb-meta.exe" -ArgumentList "--config", "$workingDir/meta/config/config_8921.toml" -NoNewWindow
    Write-Host "Server 3 started"
    Start-Sleep -Seconds 2
    Write-Host "Initialize server 1 as a single-node cluster"
    Invoke-RestMethod -Uri "http://127.0.0.1:8901/init" -Method Post -ContentType "application/json" -Body "{}"
    # & curl --silent "127.0.0.1:8901/init" -H "Content-Type: application/json" -d "{}"
    Write-Host "Server 1 is a leader now"
    Start-Sleep -Seconds 2
    Write-Host "Adding node 2 and node 3 as learners, to receive log from leader node 1"
    Invoke-RestMethod -Uri "http://127.0.0.1:8901/add-learner" -Method Post -ContentType "application/json" -Body '[2, "127.0.0.1:8911"]'
    # & curl --silent "127.0.0.1:8901/add-learner" -H "Content-Type: application/json" -d '[2, "127.0.0.1:8911"]'
    Write-Host "Server 2 is a learner now"
    Start-Sleep -Seconds 2
    Invoke-RestMethod -Uri "http://127.0.0.1:8901/add-learner" -Method Post -ContentType "application/json" -Body '[3, "127.0.0.1:8911"]'
    # & curl --silent "127.0.0.1:8901/add-learner" -H "Content-Type: application/json" -d '[3, "127.0.0.1:8921"]'
    Write-Host "Server 3 is a learner now"
    Start-Sleep -Seconds 2
    Invoke-RestMethod -Uri "http://127.0.0.1:8901/change-membership" -Method Post -ContentType "application/json" -Body '[1, 2, 3]'
    # & curl --silent "127.0.0.1:8901/change-membership" -H "Content-Type: application/json" -d '[1, 2, 3]'
    Write-Host "Server 1, 2, 3 are in the same cluster now"
    Start-Sleep -Seconds 2
    Invoke-RestMethod -Uri "http://127.0.0.1:8901/metrics" -Method Get
    # & curl --silent "127.0.0.1:8901/metrics" 
    Write-Host "meta done"
}

function Bundle {
    Write-Host "bundle..."
    Write-Host "Start cnosdb server..."
    Start-Process -FilePath "$workingDir/target/release/cnosdb.exe" -ArgumentList "run", "--config", "$workingDir/config/config_8902.toml" -NoNewWindow
    Write-Host "Server 1 started"
    Start-Process -FilePath "$workingDir/target/release/cnosdb.exe" -ArgumentList "run", "--config", "$workingDir/config/config_8912.toml" -NoNewWindow
    Write-Host "Server 2 started"
    Write-Host "bundle done"
}

function Separation {
    Write-Host "separation..."
    Write-Host "Start cnosdb server..."
    Start-Process -FilePath "$workingDir/target/release/cnosdb.exe" -ArgumentList "run", "--config", "$workingDir/config/config_8902.toml", "-M", "query" -NoNewWindow
    Write-Host "Server 1 started"
    Start-Process -FilePath "$workingDir/target/release/cnosdb.exe" -ArgumentList "run", "--config", "$workingDir/config/config_8912.toml", "-M", "tskv" -NoNewWindow
    Write-Host "Server 2 started"
    Write-Host "separation done"
}
Clean-Environment
switch ($b) {
    "main" {
        Write-Host "checkout main branch"
        # & git checkout main
        Write-Host "pull main branch"
        # & git pull
        if ($t -eq "latest") {
            Write-Host " main latest"
            $currentCommitId = & git rev-parse HEAD
            Write-Host "current commit id: $currentCommitId"
            Build
            Meta
            switch ($M) {
                "bundle" {
                    Write-Host "install main latest bundle"
                    Bundle
                }
                "separation" {
                    Write-Host "install main latest npm"
                    Separation
                }
                default {
                    Write-Host "install main latest bundle"
                    Bundle
                }
            }
        } else {
            Write-Host " main tag: $t"
            & git checkout $t
            $currentCommitId = git rev-parse HEAD
            Write-Host "current commit id: $currentCommitId"
            Build
            Meta
            switch ($M) {
                "bundle" {
                    Write-Host "install main $t bundle"
                    Bundle
                }
                "separation" {
                    Write-Host "install main $t npm"
                    Separation
                }
                default {
                    Write-Host "install main $t bundle"
                    Bundle
                }
            }
        }
    }
    "LTS/2.3" {
        Write-Host "checkout LTS/2.3 branch"
        git checkout LTS/2.3
        if ($t -eq "latest") {
            Write-Host " LTS/2.3 latest"
            $currentCommitId = & git rev-parse HEAD
            Write-Host "current commit id: $currentCommitId"
            Build
            Meta
            switch ($M) {
                "bundle" {
                    Write-Host "install main latest bundle"
                    Bundle
                }
                "separation" {
                    Write-Host "install main latest npm"
                    Separation
                }
                default {
                    Write-Host "install main latest bundle"
                    Bundle
                }
            }
        } else {
            Write-Host " main tag: $t"
            & git checkout $t
            $currentCommitId = git rev-parse HEAD
            Write-Host "current commit id: $currentCommitId"
            Build
            Meta
            switch ($M) {
                "bundle" {
                    Write-Host "install main $t bundle"
                    Bundle
                }
                "separation" {
                    Write-Host "install main $t npm"
                    Separation
                }
                default {
                    Write-Host "install main $t bundle"
                    Bundle
                }
            }
        }
    }
    default {
        Write-Host "default"
    }
}