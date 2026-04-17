// 声明 package xxx
// 1. package main 表示一个将要生成一个可执行文件的包，必须包含一个 main 函数作为程序入口点。
// 如果没有main函数，编译时将会报错：function main is undeclared（未申报） in the main package
// 如果前面没有package main，在编译时会报错：xxx is not a main package
// 2. package xxx 表示这里不是一个可执行的文件，而是一个库文件，不能直接执行，但是可以被其他代码导入使用。
package main

// 导入 import
// 1. 基础导入
// import "fmt"
// import "math/rand"
// import "time"
// 2. 组合导入（推荐）
// 3. 导入库文件分三类：标准库，第三方库，自定义库;推荐顺序导入
import (
	"fmt"  // 标准库，格式化输入，输出等
	// f "fmt" // 4. 导入时重命名，使用f代替fmt
	"math/rand"  // 标准库，用于生成伪随机数
	"time" // 标准库，提供时间相关功能
	// _ "github.com/lib/pq" // 5. 匿名导入，表示只执行包的init函数，不包括其他内容。
	// . "fmt" // 6. 点导入（不推荐）可以直接使用fmt中的函数。但是可能会造成命名冲突，降低代码可读性。
)

/*
// 结构体 struct
// 特点： 组合数据，内存连续，无隐式开销。
// 封装： golang通过首字母控制访问
	// 大写开头：public，外部包可访问
	// 小写开头：private，仅包内可访问
// 举例：
type Node struct {
	IP string
	Port int
	User string
	IsActive bool
}
// 绑定方法
// 这是一个接收者函数，相当于给Node结构体添加了一个方法Connect，可以通过Node实例调用。
func (n *Node) Connect() {
	fmt.Printf("Connecting to %s:%d ...\n", n.IP, n.Port)
}
// 组合代替继承
	讲一个结构体嵌入另一个结构体，实现继承的效果。匿名嵌入
type AdminNode struct {
	Node // 匿名嵌入
	Level int
}
*/
// Ancestor 定义家族节点
type Ancestor struct {
	Generation int     // 第几代
	Resources  float64 // 资源值 (0-100, 越低越穷)
	Name       string
}

func main() {
	// Println("这是一个点导入（不推荐）")
	// f.Println("using alias for fmt") // 使用别名f代替fmt
	rand.Seed(time.Now().UnixNano())

	// 初始状态：假设你是宋朝的一个中产阶级
	currentFamily := []Ancestor{
		{Generation: 1, Resources: 50, Name: "始祖"},
	}

	fmt.Println("--- 家族谱系 900 年生存模拟开始 ---")

	for gen := 1; gen <= 30; gen++ {
		var nextGeneration []Ancestor

		// 每一代面临的社会环境
		event := getYearlyEvent()
		fmt.Printf("第 %d 代 | 环境: %s | 当前家族人数: %d\n", gen, event.desc, len(currentFamily))

		for _, p := range currentFamily {
			// 计算生存概率：资源越低，死于灾荒概率越高
			survivalRate := 0.7 + (p.Resources / 200.0) - event.mortality
			if rand.Float64() > survivalRate {
				continue // 该分支断绝
			}

			// 计算后代数量 (论迹：穷人孩子少且难存活)
			childCount := 0
			if p.Resources > 70 {
				childCount = rand.Intn(4) + 1 // 1-4个
			} else if p.Resources > 30 {
				childCount = rand.Intn(3)     // 0-2个
			} else {
				childCount = rand.Intn(2)     // 0-1个 (极易绝户)
			}

			for i := 0; i < childCount; i++ {
				// 阶层流动：每一代资源会随机波动 (均值回归)
				newRes := p.Resources*0.9 + rand.Float64()*20 - 5 
				if newRes > 100 { newRes = 100 }
				if newRes < 0 { newRes = 0 }

				nextGeneration = append(nextGeneration, Ancestor{
					Generation: gen + 1,
					Resources:  newRes,
				})
			}
		}

		if len(nextGeneration) == 0 {
			fmt.Printf("❌ 家族在第 %d 代不幸灭绝。历史是残酷的。\n", gen)
			return
		}
		currentFamily = nextGeneration
	}

	fmt.Printf("\n🏆 奇迹！你的家族通过了30代考验，现代幸存后代数: %d\n", len(currentFamily))
	fmt.Println("这证明了你的祖先在每一个至暗时刻都跑赢了概率。")
}

type event struct {
	desc      string
	mortality float64
}

func getYearlyEvent() event {
	r := rand.Float64()
	switch {
	case r < 0.05:
		return event{"【大和战乱】全境随机抹除", 0.6}
	case r < 0.15:
		return event{"【饥荒】赤贫阶层大面积断绝", 0.3}
	case r < 0.25:
		return event{"【瘟疫】无差别随机淘汰", 0.2}
	default:
		return event{"【平稳时期】低概率损耗", 0.05}
	}
}
