The Travel Management System - Admin Dashboard is a console application designed to help travel company administrators manage customer trip data efficiently. The system supports monitoring...oring of upcoming travel dates, destination summaries, tier memberships, and booking details including payment methods.

👥 Stakeholders  
This application is designed for administrative staff in travel companies, particularly those responsible for tracking trip schedules, customer membership tiers, and generating summaries or reports. It suits individuals or teams managing travel bookings in a tourism service environment.

🏢 Target Industry  
This system is primarily tailored for businesses in the travel and tourism industry, especially companies offering domestic or international trip packages that require detailed record keeping and customer data coordination.

🔍 Application Overview  
The application provides a text-based interface with several features, such as:

- View complete travel data in a tabular format  
- Summarize tier memberships and most popular destinations  
- List names of travelers departing within the next 3 days  
- Filter travel records by tier or destination  
- Add new customer travel records or add more trips to existing customers  
- Search for travel data by ID, name, or destination  
- Delete records by ID, name, or clear the entire database  
- Includes validation and confirmation prompts to minimize input errors

🧰 Technologies Used  
- **Libraries**:  
  - `datetime` – for handling travel dates  
  - `tabulate` – to display structured data in the console  

▶️ How to Run  
1. Ensure Python 3 is installed.  
2. Install dependencies if needed:  
   ```bash
   pip install tabulate
