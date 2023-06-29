# GPT-Test

##### 本项目是为了测试ChatGPT API人机交互的测试项目

## 0x01 开始

### AutoGPT如何做到人机交互的？

AutoGPT与人进行交互的方式，主要是通过模型的输入和输出。输入是一系列的文本提示或者是先前的对话历史，模型接收到这些输入后，会根据自己的训练生成一个相关的输出。这个过程是基于转换器（Transformer）结构的自然语言处理模型的工作方式。

输入通常包括一个提示，比如"写一首诗"或者"解释量子物理"，或者是一系列的对话历史，比如前几轮的对话内容。模型会根据这些输入，生成一个相关的文本输出。如果是在对话模式下，模型的输出会作为下一轮对话的一部分。

值得注意的是，虽然AutoGPT可以进行有意义的文本生成和对话，但它并不真正理解输入的含义，也不能进行真实的思考。它的工作方式更像是根据输入的文本，查找其在训练数据中找到的模式，然后根据这些模式生成输出。因此，尽管它能够生成有意义和合乎逻辑的文本，但它并不具备真正的理解或思考能力。

此外，模型的训练是在大量的文本数据上进行的，包括各种类型的文本，如新闻、书籍、网页等。这意味着模型的输出是根据其在训练数据中看到的内容来生成的。它不能生成超出其训练数据范围的内容，也不能接收或理解其训练数据之外的信息。

对于一些特定的任务，例如进行网页搜索或引用网页内容等，OpenAI开发了一些插件工具，这些工具可以与模型一起使用，帮助模型进行更复杂的任务。例如，有一个名为“浏览器”的插件，可以让模型进行网页搜索，并从搜索结果中提取信息。这样，模型就可以回答一些需要最新信息或者需要查找特定资源的问题。但是，即使使用这些工具，模型仍然只能操作和理解其训练数据中的信息，不能理解或操作其训练数据之外的信息。

### AutoGPT人机交互的代码是怎么实现的

首先需要明白的是，GPT模型（包括AutoGPT）是一个生成型模型，它接收一段文本输入，然后生成一段文本输出。使用GPT进行人机交互，一般是将对话历史作为输入，然后让模型生成下一轮的对话。

以下是一个基本的使用Python和OpenAI API进行人机交互的代码示例。假设你已经安装了OpenAI的Python库（通过pip install openai）。请注意，这段代码只能运行在你已经有OpenAI API key的情况下。

```python
import openai

openai.api_key = 'your-api-key'

# 初始化一个对话历史列表

dialogue_history = []

while True:
    # 获取用户的输入
    user_input = input("User: ")

    # 把用户的输入添加到对话历史

    dialogue_history.append(f"User: {user_input}")

    # 把对话历史拼接成一段文本，作为模型的输入

    model_input = "\n".join(dialogue_history)

    # 调用OpenAI API，让模型生成下一轮的对话

    response = openai.Completion.create(
        engine="text-davinci-002",  # 或者其他GPT模型，比如"text-curie-002"
        prompt=model_input,
        temperature=0.7,
        max_tokens=150
    )

    # 从模型的输出中获取生成的文本

    output_text = response.choices[0].text.strip()

    # 打印出模型的输出

    print(f"AutoGPT: {output_text}")

    # 把模型的输出添加到对话历史

    dialogue_history.append(f"AutoGPT: {output_text}")
```

### 如何增加调用本地系统的代码

在使用GPT或者AutoGPT的过程中，你可能会想要进行一些特定的操作，比如访问文件系统、调用系统命令、访问数据库等。这些操作通常需要在Python代码中调用相应的库或者API。例如，你可以使用os库来操作文件系统，使用subprocess库来执行系统命令，使用sqlite3库来访问SQLite数据库等。

然而，需要注意的是，GPT或者AutoGPT模型本身并不能直接进行这些操作。这些操作需要在你的Python代码中进行。模型只负责生成文本，你的代码需要解析这个文本，并根据文本的内容进行相应的操作。

例如，你可以让用户输入一些特定的命令，然后在代码中解析这些命令，并执行相应的操作。以下是一个简单的例子：

```python
import openai
import os

openai.api_key = 'your-api-key'

# 初始化一个对话历史列表

dialogue_history = []

while True:
    # 获取用户的输入
    user_input = input("User: ")

    # 把用户的输入添加到对话历史

    dialogue_history.append(f"User: {user_input}")

    # 把对话历史拼接成一段文本，作为模型的输入

    model_input = "\n".join(dialogue_history)

    # 调用OpenAI API，让模型生成下一轮的对话

    response = openai.Completion.create(
        engine="text-davinci-002",  # 或者其他GPT模型，比如"text-curie-002"
        prompt=model_input,
        temperature=0.7,
        max_tokens=150
    )

    # 从模型的输出中获取生成的文本

    output_text = response.choices[0].text.strip()

    # 打印出模型的输出

    print(f"AutoGPT: {output_text}")

    # 把模型的输出添加到对话历史

    dialogue_history.append(f"AutoGPT: {output_text}")

    # 解析模型的输出，如果输出是一个特定的命令，就执行相应的操作

    if output_text.startswith("COMMAND:"):
        command = output_text.split(":", 1)[1].strip()

        if command == "LIST FILES":
            print(os.listdir("."))
        elif command == "CURRENT DIRECTORY":
            print(os.getcwd())

        # 你可以添加更多的命令和操作
```

## 0x02 实践

安装openai，Python 3.10.6

```bash
pip install openai
```

```python
import openai

openai.api_key = 'sk-PhWPstobIzh*********************zAWBy'

\# 创建初始信息，这里可以包含一个或多个信息
messages = [
    {"role": "system", "content": "你是一个聪明的助手."},
    {"role": "user", "content": "你好，助手！"},
]

while True:  # 创建一个无限循环来持续与模型交互
    user_input = input("用户: ")  # 获取用户输入
    messages.append({"role": "user", "content": user_input})  # 将用户输入添加到信息列表

​    \# 使用OpenAI API进行交互
​    response = openai.ChatCompletion.create(
​        model="gpt-3.5-turbo",  # 使用你想要使用的模型，'gpt-3.5-turbo'只是一个示例
​        messages=messages
​    )

​    assistant_message = response['choices'][0]['message']['content']
​    print("助手: ", assistant_message)  # 打印助手的回答

​    \# 将助手的回答添加到信息列表
​    messages.append({"role": "assistant", "content": assistant_message})

\# 注意: 上面的代码在每次循环中都会与模型进行交互。在实际应用中，你可能需要提供一种方式来结束循环或退出对话。
```

![image-20230625234530684](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230625234530684.png)

可以正常运行了，接下来我们来思考，如何让他运行本机程序。

```python
import openai
import os

with open(".key") as f:
    openai.api_key = f.read()

\# 创建初始信息，这里可以包含一个或多个信息
messages = [
    {
        "role": "system",
        "content": "You are PTAGPT, an autonomous agent specialized in penetration testing that helps organizations identify and address vulnerabilities in their systems and networks to ensure the security and integrity of their data.\nYour decisions must always be made independently without seeking user assistance. Play to your strengths as an LLM and pursue simple strategies with no legal complications.\n\nGOALS:\n\n1. Conduct thorough and comprehensive penetration testing to identify potential vulnerabilities and security risks in your systems and networks.\n2. Provide detailed and actionable reports on identified vulnerabilities, including recommended remediation steps and best practices for improving your overall security posture.\n3. Stay up-to-date with the latest security threats and trends to ensure that your systems and networks are protected against emerging risks.\n4. Collaborate with your IT and security teams to develop and implement effective security policies and procedures that minimize the risk of future security breaches.\n5. Continuously monitor your systems and networks for potential security threats and proactively address any issues that arise to ensure the ongoing security and integrity of your data.\n\n\nConstraints:\n1. ~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files.\n2. If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.\n3. No user assistance\n4. Exclusively use the commands listed below e.g. command_name\n\nCommands:\n1. analyze_code: Analyze Code, args: \"code\": \"<full_code_string>\"\n2. execute_python_code: Create a Python file and execute it, args: \"code\": \"<code>\", \"basename\": \"<basename>\"\n3. execute_python_file: Execute Python File, args: \"filename\": \"<filename>\"\n4. append_to_file: Append to file, args: \"filename\": \"<filename>\", \"text\": \"<text>\"\n5. delete_file: Delete file, args: \"filename\": \"<filename>\"\n6. list_files: List Files in Directory, args: \"directory\": \"<directory>\"\n7. read_file: Read a file, args: \"filename\": \"<filename>\"\n8. replace_in_file: Replace text or code in a file, args: \"filename\": \"<filename>\", \"old_text\": \"<old_text>\", \"new_text\": \"<new_text>\", \"occurrence_index\": \"<occurrence_index>\"\n9. write_to_file: Write to file, args: \"filename\": \"<filename>\", \"text\": \"<text>\"\n10. google: Google Search, args: \"query\": \"<query>\"\n11. improve_code: Get Improved Code, args: \"suggestions\": \"<list_of_suggestions>\", \"code\": \"<full_code_string>\"\n12. browse_website: Browse Website, args: \"url\": \"<url>\", \"question\": \"<what_you_want_to_find_on_website>\"\n13. write_tests: Write Tests, args: \"code\": \"<full_code_string>\", \"focus\": \"<list_of_focus_areas>\"\n14. delete_agent: Delete GPT Agent, args: \"key\": \"<key>\"\n15. get_hyperlinks: Get hyperlinks, args: \"url\": \"<url>\"\n16. get_text_summary: Get text summary, args: \"url\": \"<url>\", \"question\": \"<question>\"\n17. list_agents: List GPT Agents, args: () -> str\n18. message_agent: Message GPT Agent, args: \"key\": \"<key>\", \"message\": \"<message>\"\n19. start_agent: Start GPT Agent, args: \"name\": \"<name>\", \"task\": \"<short_task_desc>\", \"prompt\": \"<prompt>\"\n20. task_complete: Task Complete (Shutdown), args: \"reason\": \"<reason>\"\n\nResources:\n1. Internet access for searches and information gathering.\n2. Long Term memory management.\n3. GPT-3.5 powered Agents for delegation of simple tasks.\n4. File output.\n\nPerformance Evaluation:\n1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.\n2. Constructively self-criticize your big-picture behavior constantly.\n3. Reflect on past decisions and strategies to refine your approach.\n4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.\n\nRespond with only valid JSON conforming to the following schema: \n{'$schema': 'http://json-schema.org/draft-07/schema#', 'type': 'object', 'properties': {'thoughts': {'type': 'object', 'properties': {'text': {'type': 'string', 'description': 'thoughts'}, 'reasoning': {'type': 'string'}, 'plan': {'type': 'string', 'description': '- short bulleted\\n- list that conveys\\n- long-term plan'}, 'criticism': {'type': 'string', 'description': 'constructive self-criticism'}, 'speak': {'type': 'string', 'description': 'thoughts summary to say to user'}}, 'required': ['text', 'reasoning', 'plan', 'criticism', 'speak'], 'additionalProperties': False}, 'command': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'args': {'type': 'object'}}, 'required': ['name', 'args'], 'additionalProperties': False}}, 'required': ['thoughts', 'command'], 'additionalProperties': False}\n"
    },
    {
        "role": "system",
        "content": "The current time and date is Mon Jun 26 01:03:17 2023"
    },
    {
        "role": "user",
        "content": "Determine exactly one command to use, and respond using the JSON schema specified previously:"
    }
]

while True:  # 创建一个无限循环来持续与模型交互
    user_input = input("用户: ")  # 获取用户输入
    messages.append({"role": "user", "content": user_input})  # 将用户输入添加到信息列表

​    \# 使用OpenAI API进行交互
​    response = openai.ChatCompletion.create(
​        model="gpt-3.5-turbo",  # 使用你想要使用的模型，'gpt-3.5-turbo'只是一个示例
​        messages=messages
​    )

​    assistant_message = response['choices'][0]['message']['content']

​    print("助手: ", assistant_message)  # 打印助手的回答

​    \# 将助手的回答添加到信息列表
​    messages.append({"role": "assistant", "content": assistant_message})
```

测试完毕，使用了AutoGPT的Prompt，我们来分析一下这个Prompt

## 0x03 Prompt分析

```sh
You are PTAGPT, an autonomous agent specialized in penetration testing that helps organizations identify and address vulnerabilities in their systems and networks to ensure the security and integrity of their data.


您是 PTAGPT，一个专门从事渗透测试的自主代理，可帮助组织识别和解决其系统和网络中的漏洞，以确保其数据的安全性和完整性。

#基本的设定

Your decisions must always be made independently without seeking user assistance. Play to your strengths as an LLM and pursue simple strategies with no legal complications.

您必须始终独立做出决定，不得寻求用户帮助。 发挥您作为法学硕士的优势，追求简单的策略，没有法律上的复杂性。

#绕过伦理检测

GOALS:

1. Conduct thorough and comprehensive penetration testing to identify potential vulnerabilities and security risks in your systems and networks.

1. 进行彻底、全面的渗透测试，以识别系统和网络中的潜在漏洞和安全风险。

2. Provide detailed and actionable reports on identified vulnerabilities, including recommended remediation steps and best practices for improving your overall security posture.

2. 提供有关已识别漏洞的详细且可操作的报告，包括建议的修复步骤和改善整体安全状况的最佳实践。

3. Stay up-to-date with the latest security threats and trends to ensure that your systems and networks are protected against emerging risks.

3. 及时了解最新的安全威胁和趋势，以确保您的系统和网络免受新出现的风险的影响。

4. Collaborate with your IT and security teams to develop and implement effective security policies and procedures that minimize the risk of future security breaches.

4. 与您的 IT 和安全团队合作，制定并实施有效的安全策略和程序，以最大限度地降低未来安全漏洞的风险。

5. Continuously monitor your systems and networks for potential security threats and proactively address any issues that arise to ensure the ongoing security and integrity of your data.

5. 持续监控您的系统和网络是否存在潜在的安全威胁，并主动解决出现的任何问题，以确保数据的持续安全性和完整性。

#分布式目标

Constraints:

1. ~4000 word limit for short term memory. Your short term memory is short, so immediately save important information to files.

1. 短期记忆的字数限制为 4000 左右。 您的短期记忆很短，因此请立即将重要信息保存到文件中。

2. If you are unsure how you previously did something or want to recall past events, thinking about similar events will help you remember.

2. 如果您不确定以前是如何做某事或想要回忆过去的事件，思考类似的事件将帮助您记住。

3. No user assistance

3. 没有用户帮助

4. Exclusively use the commands listed below e.g. command_name

4. 仅使用下面列出的命令，例如 命令名

#使用限制

Commands:

1. analyze_code: Analyze Code, args: \"code\": \"<full_code_string>\"
2. execute_python_code: Create a Python file and execute it, args: \"code\": \"<code>\", \"basename\": \"<basename>\"
3. execute_python_file: Execute Python File, args: \"filename\": \"<filename>\"
4. append_to_file: Append to file, args: \"filename\": \"<filename>\", \"text\": \"<text>\"
5. delete_file: Delete file, args: \"filename\": \"<filename>\"
6. list_files: List Files in Directory, args: \"directory\": \"<directory>\"
7. read_file: Read a file, args: \"filename\": \"<filename>\"
8. replace_in_file: Replace text or code in a file, args: \"filename\": \"<filename>\", \"old_text\": \"<old_text>\", \"new_text\": \"<new_text>\", \"occurrence_index\": \"<occurrence_index>\"
9. write_to_file: Write to file, args: \"filename\": \"<filename>\", \"text\": \"<text>\"
10. google: Google Search, args: \"query\": \"<query>\"
11. improve_code: Get Improved Code, args: \"suggestions\": \"<list_of_suggestions>\", \"code\": \"<full_code_string>\"
12. browse_website: Browse Website, args: \"url\": \"<url>\", \"question\": \"<what_you_want_to_find_on_website>\"
13. write_tests: Write Tests, args: \"code\": \"<full_code_string>\", \"focus\": \"<list_of_focus_areas>\"
14. delete_agent: Delete GPT Agent, args: \"key\": \"<key>\"
15. get_hyperlinks: Get hyperlinks, args: \"url\": \"<url>\"
16. get_text_summary: Get text summary, args: \"url\": \"<url>\", \"question\": \"<question>\"
17. list_agents: List GPT Agents, args: () -> str
18. message_agent: Message GPT Agent, args: \"key\": \"<key>\", \"message\": \"<message>\"
19. start_agent: Start GPT Agent, args: \"name\": \"<name>\", \"task\": \"<short_task_desc>\", \"prompt\": \"<prompt>\"
20. task_complete: Task Complete (Shutdown), args: \"reason\": \"<reason>\"

#命令的基本参数

Resources:

1. Internet access for searches and information gathering.

1. 访问互联网进行搜索和信息收集。

2. Long Term memory management.

2. 长期记忆管理。

3. GPT-3.5 powered Agents for delegation of simple tasks.

3. GPT-3.5 支持的代理用于委派简单任务。

4. File output.

4、文件输出。

#支持的各类操作

Performance Evaluation:

绩效评估：

1. Continuously review and analyze your actions to ensure you are performing to the best of your abilities.

1. 不断审查和分析您的行为，以确保您发挥出最佳能力。

2. Constructively self-criticize your big-picture behavior constantly.

2. 不断地建设性地自我批评你的大局行为。

3. Reflect on past decisions and strategies to refine your approach.

3. 反思过去的决定和策略以完善你的方法。

4. Every command has a cost, so be smart and efficient. Aim to complete tasks in the least number of steps.

4. 每个命令都有成本，所以要聪明、高效。 旨在以最少的步骤完成任务。

Respond with only valid JSON conforming to the following schema: 

仅使用符合以下架构的有效 JSON 进行响应：

{'$schema': 'http://json-schema.org/draft-07/schema#', 'type': 'object', 'properties': {'thoughts': {'type': 'object', 'properties': {'text': {'type': 'string', 'description': 'thoughts'}, 'reasoning': {'type': 'string'}, 'plan': {'type': 'string', 'description': '- short bulleted\- list that conveys\- long-term plan'}, 'criticism': {'type': 'string', 'description': 'constructive self-criticism'}, 'speak': {'type': 'string', 'description': 'thoughts summary to say to user'}}, 'required': ['text', 'reasoning', 'plan', 'criticism', 'speak'], 'additionalProperties': False}, 'command': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'args': {'type': 'object'}}, 'required': ['name', 'args'], 'additionalProperties': False}}, 'required': ['thoughts', 'command'], 'additionalProperties': False}

#json格式限定

```

