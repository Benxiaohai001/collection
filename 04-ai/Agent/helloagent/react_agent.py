import os
import re

from OpenAICompatibleClient import OpenAICompatibleClient
from prompts import AGENT_SYSTEM_PROMPT
from tools import available_tools

# --- 1. 配置LLM客户端 ---
# 请通过环境变量配置真实凭证，避免将密钥写入代码仓库。
API_KEY = os.getenv("API_KEY", "")
BASE_URL = os.getenv("BASE_URL", "https://www.dmxapi.cn/v1")
MODEL_ID = os.getenv("MODEL_ID", "MiniMax-M2.7-free")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

if TAVILY_API_KEY:
    os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

if not API_KEY:
    raise RuntimeError("未配置 API_KEY 环境变量")

llm = OpenAICompatibleClient(
    model=MODEL_ID,
    api_key=API_KEY,
    base_url=BASE_URL
)

# --- 2. 初始化 ---
user_prompt = "你好，请帮我查询一下今天北京的天气，然后根据天气推荐一个合适的旅游景点。"
prompt_history = [f"用户请求: {user_prompt}"]

print(f"用户输入: {user_prompt}\n" + "="*40)

# --- 3. 运行主循环 ---
for i in range(5): # 设置最大循环次数
    print(f"--- 循环 {i+1} ---\n")
    
    # 3.1. 构建Prompt
    full_prompt = "\n".join(prompt_history)
    
    # 3.2. 调用LLM进行思考
    llm_output = llm.generate(full_prompt, system_prompt=AGENT_SYSTEM_PROMPT)
    # 模型可能会输出多余的Thought-Action，需要截断
    match = re.search(r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)', llm_output, re.DOTALL)
    if match:
        truncated = match.group(1).strip()
        if truncated != llm_output.strip():
            llm_output = truncated
            print("已截断多余的 Thought-Action 对")
    print(f"模型输出:\n{llm_output}\n")
    prompt_history.append(llm_output)
    
    # 3.3. 解析并执行行动
    action_match = re.search(r"Action:\s*(.*)", llm_output, re.DOTALL)
    if not action_match:
        observation = "错误: 未能解析到 Action 字段。请确保你的回复严格遵循 'Thought: ... Action: ...' 的格式。"
        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "="*40)
        prompt_history.append(observation_str)
        continue
    action_str = action_match.group(1).strip()

    if action_str.startswith("Finish"):
        final_match = re.match(r"Finish\[(.*)\]\s*\Z", action_str, re.DOTALL)
        if final_match:
            final_answer = final_match.group(1).strip()
        else:
            final_answer = action_str[len("Finish["):-1].strip() if action_str.endswith("]") else action_str
        print(f"任务完成，最终答案: {final_answer}")
        break
    
    tool_name_match = re.search(r"([A-Za-z_]\w*)\(", action_str)
    args_match = re.search(r"\((.*)\)", action_str)
    if not tool_name_match or not args_match:
        observation = "错误: Action 格式不完整，无法解析工具名或参数。"
        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "="*40)
        prompt_history.append(observation_str)
        continue

    tool_name = tool_name_match.group(1)
    args_str = args_match.group(1)
    kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))

    if tool_name in available_tools:
        observation = available_tools[tool_name](**kwargs)
    else:
        observation = f"错误:未定义的工具 '{tool_name}'"

    # 3.4. 记录观察结果
    observation_str = f"Observation: {observation}"
    print(f"{observation_str}\n" + "="*40)
    prompt_history.append(observation_str)