import nextcord
from nextcord.ext import commands, tasks
import dotenv
import os
from CourseChecker import CourseChecker

dotenv.load_dotenv("tokens.env")
intents = nextcord.Intents.all()

courses_to_scrape: list[CourseChecker]

courses_to_scrape = []

ttb = commands.Bot(command_prefix='ttb', intents=intents)

@ttb.event
async def on_ready():
    print(f'{ttb.user} has connected to Discord!')

@tasks.loop(seconds=30)
async def scrape():
    for i in range(len(courses_to_scrape)):
        course = courses_to_scrape[i]
        if course.scrape():
            # We want to DM the user
            user = ttb.get_user(course.user)
            await user.send(f"Your course {course._course_code} {course._activity} has a spot open!")
            courses_to_scrape.pop(i)
            
scrape.start()

@ttb.slash_command(name="add", description="Add a course to be tracked by the bot")    
async def add(interaction: nextcord.Interaction, course_code: str, course_title: str, activity: str, session: str):
    course = CourseChecker(course_code, course_title, session, activity, interaction.user.id)
    courses_to_scrape.append(course)
    await interaction.response.send_message(f"Added {course_code} {activity} {session} to the list of courses to be tracked", ephemeral=True)

        
ttb.run(os.getenv('DISCORD'))
