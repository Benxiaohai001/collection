import os
from tavily import TavilyClient

from typing import Dict, Any

class ToolExecutor:
    """
    一个工具执行器，负责管理和执行工具。
    """
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}

    def registerTool(self, name: str, description: str, func: callable):
        """
        向工具箱中注册一个新工具。
        """
        if name in self.tools:
            print(f"警告:工具 '{name}' 已存在，将被覆盖。")
        self.tools[name] = {"description": description, "func": func}
        print(f"工具 '{name}' 已注册。")

    def getTool(self, name: str) -> callable:
        """
        根据名称获取一个工具的执行函数。
        """
        return self.tools.get(name, {}).get("func")

    def getAvailableTools(self) -> str:
        """
        获取所有可用工具的格式化描述字符串。
        """
        return "\n".join([
            f"- {name}: {info['description']}" 
            for name, info in self.tools.items()
        ])



def search(query: str) -> str:
    """
    一个基于 Tavily 的实战网页搜索引擎工具。
    免手机号验证，智能聚合多源结果，完美适配大模型提示词。
    """
    print(f"🔍 正在执行 [Tavily] 网页搜索: {query}")
    try:
        # 从环境变量获取密钥（控制台复制的 tvly- 开头字符串）
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "错误: TAVILY_API_KEY 未在 .env 文件中配置。"

        # 初始化客户端
        tavily_client = TavilyClient(api_key=api_key)
        
        # 执行搜索：开启动态高级搜索，并要求直接生成总结答案
        response = tavily_client.search(
            query=query,
            search_depth="advanced",   # 深度搜索，可选: basic / advanced / fast / ultra-fast
            include_answer=True,       # 强制让 Tavily 结合全网结果融合成一段直接答案
            max_results=3              # 限制返回前 3 个最相关的网页
        )
        
        # 智能解析优先：如果 Tavily 已经融合成了一段直接答案，优先返回它
        if response.get("answer"):
            return f"【AI 聚合答案】\n{response['answer']}"
            
        # 如果没有直接答案，则拼接提取出来的干净网页文本
        results = response.get("results", [])
        if results:
            snippets = [
                f"[{i+1}] {res.get('title', '')}\nURL: {res.get('url', '')}\n内容概要: {res.get('content', '')}"
                for i, res in enumerate(results)
            ]
            return "\n\n".join(snippets)
        
        return f"对不起，没有找到关于 '{query}' 的信息。"

    except Exception as e:
        return f"搜索时发生错误: {e}"


# --- 工具初始化与使用示例 ---
if __name__ == '__main__':
    # 1. 初始化工具执行器
    toolExecutor = ToolExecutor()

    # 2. 注册我们的实战搜索工具
    search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    toolExecutor.registerTool("Search", search_description, search)
    
    # 3. 打印可用的工具
    print("\n--- 可用的工具 ---")
    print(toolExecutor.getAvailableTools())

    # 4. 智能体的Action调用，这次我们问一个实时性的问题
    print("\n--- 执行 Action: Search['英伟达最新的GPU型号是什么'] ---")
    tool_name = "Search"
    tool_input = "英伟达最新的GPU型号是什么"

    tool_function = toolExecutor.getTool(tool_name)
    if tool_function:
        observation = tool_function(tool_input)
        print("--- 观察 (Observation) ---")
        print(observation)
    else:
        print(f"错误:未找到名为 '{tool_name}' 的工具。")