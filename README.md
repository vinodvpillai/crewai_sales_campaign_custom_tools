# Sales Campaign Customer Agentic Automation

This is a Sales Campaign Customer Agentic automation application developed using the **CrewAI** framework. It is designed to assist sales teams in automating and enhancing customer engagement through intelligent lead profiling and personalized outreach strategies. The application leverages multiple tools for data analysis and communication, providing sales representatives with comprehensive insights and tailored communication drafts.

![](https://github.com/vinodvpillai/crewai_report_generation_app/blob/master/resources/output.gif)
## Project Structure

The repository consists of the following key files:

```bash
crewai-report-generation-app
├── .gitignore Specifies files and directories to ignore in Git
├── pyproject.toml   Project configuration and dependencies
├── README.md  Project documentation
├── .env Environment variables
└── src/ Source code directory
    └── my_project/  Main application package
        ├── __init__.py Marks the directory as a Python package
        ├── main.py  Main application script
        ├── crew.py  Crew-related functionalities
        ├── tools/   Custom tools directory
        │ ├── custom_tool.py  Custom tool implementation
        │ └── __init__.py  Marks tools directory as a package
        └── config/  Configuration files directory
            ├── agents.yaml   Agent configurations
            └── tasks.yaml Task configurations
```
### 1. `crew.py`
Defines the `CrewaiSalesCampaignCustomToolsCrew` class, integrating various CrewAI tools and defining agents and tasks:
- **Agents**:
  - `sales_rep_agent`: Identifies high-value leads.
  - `lead_sales_rep_agent`: Crafts personalized, engaging communications for outreach.
- **Tasks**:
  - `lead_profiling_task`: Compiles a detailed lead profile.
  - `personalized_outreach_task`: Develops a personalized outreach strategy with email drafts.

### 2. `main.py`
The entry point to run and test the application locally, with functions to:
- **Run**: Execute the crew's processes with example inputs.
- **Train**: Simulate training for the agents with specified iterations.
- **Replay**: Replay a task from a specific checkpoint.
- **Test**: Test crew execution and review results.

### 3. Configuration Files
- **`tasks.yaml`**: Contains the configuration for tasks including descriptions, expected outputs, and agent assignments.
- **`agents.yaml`**: Defines the agents, their roles, goals, and backstories for more realistic task execution.


## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

> **Note**: Make sure to include `CrewAI` and any other required libraries in `requirements.txt`.

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

## How to Use

1. **Setup Configuration**:
   - Customize `agents.yaml` to define agent roles, goals, and backgrounds.
   - Update `tasks.yaml` for specifying task descriptions, tools, and expected outputs.

2. **Run the Application**:
   To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

   ```bash
   crewai run
   ```

3. **Review the Output**:
   The generated report will be displayed in the console or saved to a specified output file as defined in the `crew.py` logic.
   This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Project Overview

This application leverages **CrewAI's** capabilities for coordinating agents with distinct goals and tasks to generate reports efficiently. Each component plays a critical role:

- **Configurable Agents**: Modify agent characteristics and roles as needed.
- **Flexible Task Descriptions**: Adjust task specifics for different report types.
- **Simple Integration**: Use `main.py` to easily pass queries and trigger the workflow.
- **Scalable Logic**: Expandable to include more agents and complex tasks as your use case grows.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.
