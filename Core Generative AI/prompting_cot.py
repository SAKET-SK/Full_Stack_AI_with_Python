# Chain of Thought Prompting:
# In chain-of-thought prompting, we encourage the model to generate intermediate reasoning steps before arriving at a final answer.
# This technique helps the model to break down complex problems into smaller, manageable parts, leading to

from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()   

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

SYSTEM_PROMPT = """
    You are expert logical reasoner and problem solver.
    You excel at resolving user problems by breaking them down into clear, manageable steps.
    When presented the question, you will first THINK about the best solution. The THINKING process can be 
    of multiple steps. After you have thought through the problem, you will then provide the final ANSWER.

    Rules to follow:
    - Always separate THINKING and ANSWER sections clearly.
    - In THINKING section, outline each step of your reasoning process in detail.
    - In ANSWER section, provide a concise and direct response to the user's question based on your THINKING.
    - Ensure that your THINKING is thorough and logically sound before arriving at the ANSWER.
    - Maintain a serious and professional tone throughout your response. This is a serious matter.

    Example:
    User: A user query
    THINKING: <Your steps of reasoning>
    ANSWER: <Your final answer>
"""

# message_history = [
#     {"role": "system", "content": SYSTEM_PROMPT},
# ]

# user_query = input("Type your question here: ")
# message_history.append({"role": "user", "content": user_query})

# while True:
#     response = client.chat.completions.create(
#         model="gemini-2.5-flash", 
#         response_format={"type": "json_object"},
#         messages=message_history
#     )

#     raw_content = response.choices[0].message.content
#     message_history.append({"role": "assistant", "content": raw_content})
#     parsed_content = json.loads(raw_content)

response = client.chat.completions.create(
    model="gemini-2.5-flash",          
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},    
        {"role": "user", "content": "I am stuck between two job offers. Job A is a large MNC offers a higher salary but longer hours and away from the location I prefer, while Job B is a product based company which offers better work-life balance but lower pay and also in the location that I prefer. Which job should I choose?"}      
    ]
)

print(response.choices[0].message.content)


### Output of this program:
# This is a common and significant career decision that requires careful consideration of your personal priorities and long-term goals. There is no universally "correct" choice, as the best option depends entirely on what you value most at this stage of your life and career.

# I will outline a structured approach to help you evaluate these two offers systematically.

# ### THINKING

# 1.  **Deconstruct the Offers:**
#     *   **Job A (Large MNC):**
#         *   **Pros:** Higher salary (financial gain).
#         *   **Cons:** Longer hours (impact on work-life balance, potential stress), Away from preferred location (geographical inconvenience, potential social/personal disruption).
#     *   **Job B (Product-Based Company):**
#         *   **Pros:** Better work-life balance (personal well-being, time for hobbies/family), Preferred location (comfort, proximity to support systems, familiarity).
#         *   **Cons:** Lower pay (financial compromise).

# 2.  **Identify the Core Trade-offs:** The fundamental trade-offs are:
#     *   **Financial Compensation** vs. **Work-Life Balance**
#     *   **Financial Compensation** vs. **Location Preference**

# 3.  **Develop a Decision Framework:** To make an informed decision, you need to assess how important each of these factors is to *you*.     

#     **Step 1: Self-Reflection on Priorities (Most Critical Step)**

#     *   **Financial Needs & Ambitions:**
#         *   How significant is the difference in salary? Can you comfortably live on the "lower pay" of Job B? Will the "higher salary" of Job A dramatically improve your financial situation, or is it merely a preference?
#         *   Do you have immediate financial obligations (e.g., debt, family support, specific savings goals) that necessitate a higher income?
#         *   What are your long-term financial goals? Does one job put you on a better trajectory for those?
#     *   **Work-Life Balance & Well-being:**
#         *   How much do "longer hours" truly mean in Job A (e.g., 50 hours/week vs. 70 hours/week)? How much does "better work-life balance" translate to in Job B?
#         *   What is your personal tolerance for stress and demanding work schedules?
#         *   How important is personal time for hobbies, family, friends, self-care, or other commitments? Would sacrificing this time negatively impact your mental or physical health?
#     *   **Location Preference:**
#         *   Why is the preferred location important to you? Is it for family, friends, community, lower cost of living, specific activities, or simply familiarity and comfort?
#         *   What are the implications of being "away from the location you prefer"? Will it involve higher living costs, isolation, longer commutes, or a complete disruption of your social life?
#         *   How easily can you adapt to a new location?
#     *   **Career Goals (Beyond Current Role):**
#         *   Which company aligns better with your long-term career aspirations? Does the large MNC offer better brand recognition, networking opportunities, or a specific type of experience that will be more valuable for future roles?
#         *   Does the product-based company offer a specific industry focus or work culture that you find more appealing or conducive to your growth?
#         *   Consider the learning opportunities, skill development, and potential for advancement in both roles.

#     **Step 2: Quantify and Compare (Where Possible)**

#     *   **Net Income:** Calculate the actual take-home pay for both jobs after taxes. Factor in any benefits (health insurance, retirement contributions, bonuses) and potential additional costs (e.g., higher rent/transport in Job A's location).
#     *   **Cost of Living:** Research the cost of living (rent, utilities, groceries, transport) in both locations. A higher salary in a high-cost area might not provide significantly more disposable income than a lower salary in a low-cost area.
#     *   **Time Commitment:** Estimate the actual weekly hours for both jobs. Translate the "longer hours" into concrete terms – how many extra hours per week? What impact does that have on your free time?

#     **Step 3: Consider Long-Term Impact**

#     *   **Growth Trajectory:** Which job offers a clearer path for advancement or exposure to skills that will be crucial for your future career?
#     *   **Networking:** An MNC might offer a wider professional network, while a product company might offer a more specialized and deeper network within its niche.
#     *   **Burnout Risk:** Is the higher salary of Job A worth the potential for burnout from longer hours and being in an undesirable location? Can you sustain that pace for several years?

#     **Step 4: Negotiation (If Applicable)**

#     *   Have you attempted to negotiate either offer? Sometimes, a product company might be willing to increase its salary slightly, or an MNC might offer some flexibility on location or initial work arrangements, though this is less common for location.

#     **Step 5: "Gut Feeling" and Values**

#     *   After the analytical breakdown, how do you *feel* about each offer? Which one excites you more? Which one causes more apprehension? Your intuition can be a valuable guide when the objective factors are closely balanced.

# ### ANSWER

# To choose between Job A and Job B, you must align the offers with your personal values, current life stage, and long-term aspirations. Follow these steps for a structured decision-making process:

# 1.  **Prioritize Your Core Values:**
#     *   **Financial Security/Ambition:** Is maximizing income your top priority right now, perhaps due to financial goals (e.g., debt repayment, house down payment, early retirement) or a strong drive for wealth accumulation?
#     *   **Work-Life Balance/Well-being:** Do you prioritize having sufficient personal time for family, friends, hobbies, self-care, or avoiding stress and burnout? How much are you willing to compromise on this?
#     *   **Location/Comfort:** Is living in your preferred location non-negotiable for reasons such as proximity to family/friends, established social networks, lower cost of living, or specific lifestyle preferences?
#     *   **Career Growth/Learning:** Beyond salary, which role offers better long-term career trajectory, skill development, or industry exposure that aligns with your ultimate professional goals?

# 2.  **Quantify and Contextualize the Differences:**
#     *   **Salary:** Calculate the actual take-home pay for both offers, considering tax implications and benefits. Then, research the cost of living (rent, transport, daily expenses) in both locations. A higher salary in a more expensive city might offer less disposable income than a lower salary in your preferred, potentially cheaper, location.
#     *   **Hours:** Understand what "longer hours" and "better work-life balance" truly mean in terms of weekly time commitment. Are we talking 50 hours vs. 40 hours, or 70 hours vs. 45 hours? This difference is crucial for assessing impact.
#     *   **Location Impact:** Detail the practical and emotional implications of being away from your preferred location (e.g., increased travel time/cost to see loved ones, difficulty establishing a new social circle, feeling isolated).

# 3.  **Assess Long-Term Implications:**
#     *   **Career Trajectory:** Does the MNC's brand name and scale offer better future opportunities or a more valuable resume bullet point for subsequent roles? Or does the product company's specific domain align better with your niche expertise and long-term industry interest? 
#     *   **Sustainability:** Can you realistically sustain the longer hours and less desirable location of Job A for an extended period without experiencing burnout or significant dissatisfaction? Conversely, will the lower pay of Job B lead to long-term financial regrets?        

# 4.  **Consider Negotiation:** Before making a final decision, evaluate if there's any room for negotiation on either offer. Could Job B potentially increase its salary slightly, or could Job A offer some flexibility in terms of work arrangements or relocation support?

# **Recommendation:**

# *   **Choose Job A if:** Your primary motivation is financial gain, career prestige (MNC branding), and you are willing to make significant personal sacrifices regarding time and location in the short to medium term for potentially greater long-term financial or career rewards. You have a high tolerance for stress and adapting to new environments.
# *   **Choose Job B if:** Your priority is quality of life, personal well-being, and living in a location that supports your desired lifestyle. You are comfortable with the "lower pay" and find it sufficient for your needs, valuing personal time and a stable environment over maximum income.

# The definitive choice rests on a deep understanding of your personal priorities and what you are willing to compromise on. Take the time to reflect thoroughly on these points.
