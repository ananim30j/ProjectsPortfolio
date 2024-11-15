# DSI Social Network Database Neo4j Project

Ananya Nimbalkar 

This project creates a social networking platform specifically for DSI students and alumni, where members can share insights, seek advice, and remain connected based on shared interests, be they project-based, career-oriented, or hobby-related.

## Database Design

**Nodes:**
1. User
   - Properties: user_id, name, email, join_date, major, interests
   - Rationale: This is essential to have as it represents each person on the platform. The properties allow us to capture key information about each user, enabling personalized content, connection recommendations, and community-building features based on shared backgrounds or interests.

2. Post
   - Properties: post_id, content, created_date, topic, likes_count, comments_count, visibility
   - Rationale: Posts are the main component when interacting on social media, where it gives users a place to share insights and ask questions. The properties help identify what that post is about and during what time it was created, as well as how popular it is through likes and comments, and if it is available for everyone to see or just friends. By associating posts with topics, users can find relevant content easily, helping the platform suggest similar content or connect users with shared interests.

3. Group
   - Properties: group_id, name, description, created_date, topic
   - Rationale: Groups are key to foster community-building around specific interests, projects, or career paths. Students can join relevant groups to connect and share resources. The properties enable the creation of specialized communities within the platform.

4. Event
   - Properties: event_id, name, location, event_date, topic
   - Rationale: An event allows for networking and other learning opportunities within the DSI community. There can be workshops, meetups, or even webinars that lets users engage with one another in real-time. The properties provide detailed information on each event, letting users RSVP to plan attendance and filter by topic.

5. Badge
   - Properties: badge_id, name, description, awarded_date
   - Rationale: Badges are a great achievement and should be recognized within the DSI community, as it encourages engagement, motivating everyone to participate further and try to earn one for themselves. The properties provide information about the badge, and 'awarded_date' keeps track of when the user received the badge, allowing to celebrate users' progress over time.

**Edges:**
1. FRIEND (User) — [FRIEND] —> (User)
   - Undirected edge: Represents a mutual friendship between two users.
   - Property: since
   - Rationale: This relationship connects 2 users who chose to have a friendship/connection with each other. It facilitates direct interactions, like messaging or viewing each other's posts. The 'since' property tracks what date the friendship started, so an analysis of user engagement can be conducted over time.

2. CREATED (User) — [CREATED] —> (Post)
   - Directed edge: Points from User to Post, representing that a user created a post.
   - Rationale: This relationship links a user to the posts they have authored, enabling tracking of their contributions to the platform. It can support features like filtering posts by author or identifying the most active contributors.

3. MEMBER_OF (User) — [MEMBER_OF] —> (Group)
   - Directed edge: Points from User to Group, showing the user's membership in a specific group.
   - Property: join_date
   - Rationale: This relationship connects users to the groups they join, so community-building within specific areas of interest can occur. It can support recommendations, showing users relevant groups to join based on their interests, and allow for group-specific notifications and interactions. THe 'join_date' helps track when a user joined that group and their engagement over time.

4. ATTENDING (User) — [ATTENDING] —> (Event)
   - Directed edge: Points from User to Event, indicating that the user plans to attend the event.
   - Property: rsvp_date
   - Rationale: This relationship links users with events they plan to attend. It can support event-related features like RSVP lists, reminders, and event-based networking. 'rsvp_date' helps keep a record of when a user expressed interest in a particular event, which aids organizers in gauging interest levels and plan for their event accordingly.

5. AWARDED (User) — [AWARDED] —> (Badge)
   - Directed edge: Points from User to Badge, indicating the user has been awarded a specific badge.
   - Property: awarded_date
   - Rationale: This relationship links users to the badges they have earned, adding a layer of recognition for their activities and contributions on the platform. By connecting users to their achievements, the relationship not only highlights user contributions, but also incentivizes active participation. 'awarded_date' helps maintain a timeline of accomplishments, supporting features like notifications and showcasing recent awards on user profiles.

**Benefits:**
- Interest-based Networking: Users are able to easily find and connect with others who share the same interests, major, and/or career goals.
- Content Discovery: Users can explore posts on relevant topics, join groups, and attend events.
- Community Growth: Groups and events features foster a sense of community, encourage engagement/participation, and build meaningful connections beyond a singular post.
- User Engagement Insights: Properties and relationships can provide data on user activity, popular topics, and active community groups, which offers valuable insights for platform improvements.

**Challenges:**
- User Engagement & Retention: With a focused audience of DSI students & alumni, it may be hard to consistently have high user engagement, as they may prioritize academic and professional obligations.
- Content Moderation: All posts, comments, and messages need to be appropriate and should contribute positively to the community at all times. Continuous monitoring needs to be implemented.
- Privacy & Security: A user's personally identifiable information needs to be protected, so their profiles, interactions, and content need to be secured; there is a risk of data breaches.
- Event & Group Management: Over time, inactive groups or events might clutter the platform, making it harder for users to find the latest and most valuable content.

## Generative AI Usage
- Data Insertion: Generated the sample data, after providing it with the format of nodes, edges, and properties.
- Query Verification: Verified data was correct in terms of temporal constraints (i.e. ensuring FRIEND since dates occur after users' join_date).
- Chain of Friends Query Refinement: Provided code to iterate through nodes and relationships in the path, generating human-readable sentences to establish how 2 users may be indrectly connected.

## Setup Instructions
- Ensure Docker and Visual Studio Code are installed before proceeding to the setup.

1. Clone the Repository
    - In gitbash, enter the command: git clone https://github.com/ananim30j/ProjectsPortfolio.git
    - cd Neo4jSocialNetwork
    - Make sure this is cloned in a directory where this folder is mounted in Docker
        - If not, you need to mount it in Docker
2. Modify docker-compose.yml
    - Under 'volumes', change the path on the left side of the ':' to the directory of the parent folder of where your docker-compose.yml resides
    - Keep a note of this directory as you will need to refer to it (referred to "the project directory" in upcoming steps)
3. Start Docker Container
    - Open Docker Desktop on your machine
    - Open a terminal on your machine and cd into the project directory
    - Then enter: docker compose up
        - Starts docker container
4. Run Jupyter Notebook
   - Open up Neo4j_Query.ipynb and run the cells
      - Creates network
      - Queries variety of things, where output is displayed in pandas dataframe
   - Go to http://localhost:7474/ (found in terminal that Docker Container was started) if you want a pretty UI to run queries in
5. Stop Docker Container
   - Open a new terminal on your machine and cd into the project directory
   - Then enter: docker compose down
      - Stops docker container
   - Quit Docker Desktop