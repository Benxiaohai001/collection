package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Person struct {
	Gen    int
	Wealth float64
}

func main() {
	rand.Seed(time.Now().UnixNano())
	family := []Person{{Gen: 1, Wealth: 20}} // 起点：一个普通自耕农

	for gen := 1; gen <= 30; gen++ {
		// --- 1. 环境判定：这一代的世道如何？ ---
		envType := rand.Float64()
		mortalityBase := 0.1 // 基础死亡率 10%
		isWar := false

		if envType < 0.05 { // 5% 概率大战乱
			isWar = true
			mortalityBase = 0.6 // 死亡率飙升到 60%
		} else if envType < 0.15 { // 10% 概率瘟疫/大荒
			mortalityBase = 0.3
		}

		var nextGen []Person
		for _, p := range family {
			// --- 2. 生产与损耗 ---
			effort := rand.Float64() * 50
			leverage := 1.0 + (p.Wealth / 100.0) // 财富杠杆
			currentWealth := p.Wealth + (effort * leverage) - 15

			// --- 3. 生存校验（因果逻辑：钱能买命） ---
			// 财富越高，抵消掉的死亡率越多；战乱中，财富保护力有限
			protect := currentWealth / 500.0 
			if protect > 0.4 { protect = 0.4 } // 财富保护上限
			
			realMortality := mortalityBase - protect
			if rand.Float64() < realMortality {
				continue // 这一支断了
			}

			// --- 4. 繁衍逻辑（阶层差异） ---
			childCount := 0
			if currentWealth > 100 {
				childCount = rand.Intn(4) + 1 // 富人：1-4个
			} else if currentWealth > 30 {
				childCount = rand.Intn(3)     // 中产：0-2个
			} else if currentWealth > 10 {
				childCount = rand.Intn(2)     // 穷人：0-1个
			}

			for i := 0; i < childCount; i++ {
				// 遗产分配：长子继承制模拟
				inheritance := 0.0
				if i == 0 {
					inheritance = currentWealth * 0.7 // 长子拿70%
				} else {
					inheritance = (currentWealth * 0.3) / float64(childCount-1)
				}
				nextGen = append(nextGen, Person{Gen: gen + 1, Wealth: inheritance})
			}
		}

		if len(nextGen) == 0 {
			fmt.Printf("第 %d 代：遇到%s，家族彻底消失。\n", gen, map[bool]string{true: "战乱", false: "灾荒"}[isWar])
			return
		}
		
		family = nextGen
		fmt.Printf("第 %d 代 | 人数: %-4d | 环境: %s\n", gen, len(family), getEnvDesc(isWar, mortalityBase))
	}
	fmt.Printf("\n🏆 模拟结束！历经900年，你最终的家族规模为: %d 人\n", len(family))
}

func getEnvDesc(isWar bool, m float64) string {
	if isWar { return "🔥 兵荒马乱" }
	if m > 0.2 { return "🍂 饥荒瘟疫" }
	return "🌤️ 太平盛世"
}
