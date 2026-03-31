

param(
	[Parameter(Mandatory=$false)]
	[string]$m = '2',
	[string]$n = '1'
)


# param (
#     [Parameter(Mandatory=$false)]
#     [string]$b = "main",
#     [string]$t = "latest",
#     [string]$M = "bundle"
# )
switch ($m) {
	1 {
		Write-Output "1"
	}
	2 {
		Write-Output "2"
	}
	default {
		Write-Output "Invalid argument"
	}
}
switch ($n) {
	1 {Write-Host "n"}
	default {Write-Host "1111"}
}
<#
@echo 1;
@echo 2;
@echo 3;
@:f1 
@echo this is inner f1
@goto :eof
@f1
#>