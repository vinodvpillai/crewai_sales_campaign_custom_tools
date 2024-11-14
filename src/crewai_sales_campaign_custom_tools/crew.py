from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool
from .tools.custom_tool import SentimentAnalysisTool
from crewai import LLM # type: ignore
import os
from os.path import join, dirname
from dotenv import load_dotenv


# Load environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@CrewBase
class CrewaiSalesCampaignCustomToolsCrew():
	# DirectoryReadTool - Allows agents to read particular directory (instructions) in the local. Here we will add multiple files with necessary instructions
	directory_read_tool = DirectoryReadTool(directory='./instructions')
	# FileReadTool - Allows agents to read files
	file_read_tool = FileReadTool()
	# SerperDevTool - Allows agents to search internet
	search_tool = SerperDevTool()
	# SentimentAnalysisTool - Its a custom tool currently not having logic we can add use it
	sentiment_analysis_tool = SentimentAnalysisTool()
 
	# LLM
	llm = LLM(model=os.getenv('GEMINI_MODEL'),api_key=os.getenv('GEMINI_API_KEY'))
 
	@agent
	def sales_rep_agent(self) -> Agent:
		return Agent(
			llm=self.llm,
			config=self.agents_config['sales_rep_agent'], # type: ignore
			verbose=True
		)

	@agent
	def lead_sales_rep_agent(self) -> Agent:
		return Agent(
			llm=self.llm,
			config=self.agents_config['lead_sales_rep_agent'], # type: ignore
			verbose=True
		)

	@task
	def lead_profiling_task(self) -> Task:
		return Task(
			config=self.tasks_config['lead_profiling_task'], # type: ignore
   			tools=[self.directory_read_tool, self.file_read_tool, self.search_tool], 
		)

	@task
	def personalized_outreach_task(self) -> Task:
		return Task(
			config=self.tasks_config['personalized_outreach_task'], # type: ignore
			tools=[self.search_tool, self.sentiment_analysis_tool], 
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CrewaiSalesCampaignCustomTools crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator # type: ignore
			tasks=self.tasks, # Automatically created by the @task decorator # type: ignore
			process=Process.sequential,
			verbose=True
		)