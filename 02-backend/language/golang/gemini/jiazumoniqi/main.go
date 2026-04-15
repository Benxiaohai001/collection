package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Ancestor 定义家族节点
type Ancestor struct {
	Generation int     // 第几代
	Resources  float64 // 资源值 (0-100, 越低越穷)
	Name       string
}

func main() {
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
