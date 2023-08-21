from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv(verbose=True, override=True)
del load_dotenv


def mermaid(input: str):
    """Convert the designated scenario into a Mermaid diagram immediately. Infer and incorporate new terms as necessary. Do not err in conveying any piece of information."""

    template = """ \
System:
Convert the designated scenario into a Mermaid diagram immediately. Infer and incorporate new terms as necessary. Do not err in conveying any piece of information.

Example Input:
The human body is composed of water. Water is imperative for human survival. Ensure this information is transmitted accurately and without omission.

Example Output:
```mermaid
graph TD
    A[Human] --> B[Water]
    B --> C[Consumption]
    C --> D[Survival]
    D --> A
    B --> F[Depletion]
    F --> G[Death]
    G --> A
```

Input:
{input}

Output:
"""
    instruction = template.format(input=input)
    llm = OpenAI(temperature=0)
    output = llm.predict(instruction)
    return output


def test_mermaid():
    output = '''\
```mermaid
graph TD
    A[Alpha] --> B[Omega]
    B --> A
    A --> C[First]
    C --> D[Last]
    D --> A
    A --> E[Beginning]
    E --> F[End]
    F --> A
```
'''
    input = 'I am the Alpha and the Omega, the First and the Last, the Beginning and the End'
    pred = mermaid(input)
    print('[Input]')
    print(input)
    print('[Expected]')
    print(output)
    print('[Actual]')
    print(pred)


def search(input: str):
    """Google Searching Engine. Ask any question and get the answer."""

    template = """ \
System:
Act like a search engine. If you do not know the information, output that there are no search results.

Example Input:
What does water consist of?

Example Output:
Water is composed of two hydrogen atoms and one oxygen atom.\n

Input:
{input}

Output:
"""
    instruction = template.format(input=input)
    llm = OpenAI(temperature=0)
    output = llm.predict(instruction)
    return output


def test_search():
    output = 'World War II ended in 1945.'
    input = 'What year did the World War II end?'
    pred = search(input)
    print('[Input]')
    print(input)
    print('[Expected]')
    print(output)
    print('[Actual]')
    print(pred)


if __name__ == '__main__':
    test_mermaid()
    test_search()