import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os






def calculate_batsman_points_per_match(player_data):
    points_per_match = []
    for index, row in player_data.iterrows():
        total_runs = row['Runs']
        total_4s = row['4s']
        total_6s = row['6s']
        player_points = total_runs
        
        if total_runs >= 30:
            player_points += 5
        if total_runs >= 50:
            player_points += 10
        
        player_points += total_4s * 1  
        player_points += total_6s * 2  
        
        points_per_match.append(player_points)
    
    return points_per_match

# Define function for calculating total points
def calculate_total_batsman_points(player_data):
    total_points = 0
    for index, row in player_data.iterrows():
        total_runs = row['Runs']
        total_4s = row['4s']
        total_6s = row['6s']
        player_points = total_runs
        
        if total_runs >= 30:
            player_points += 5
        if total_runs >= 50:
            player_points += 10
        
        player_points += total_4s * 1  
        player_points += total_6s * 2 
        
        total_points += player_points
    
    return total_points

def calculate_batsman_points_per_match(player_data):
    points_per_match = []
    for index, row in player_data.iterrows():
        total_runs = row['Runs']
        total_4s = row['4s']
        total_6s = row['6s']
        player_points = total_runs
        
  
        if total_runs >= 30:
            player_points += 5
        if total_runs >= 50:
            player_points += 10
        
    
        player_points += total_4s * 1  
        player_points += total_6s * 2  
        
        points_per_match.append(player_points)
    
    return points_per_match

def calculate_bowler_points_per_match(player_data):
    points_per_match = []
    for index, row in player_data.iterrows():
        wickets = row['W']
        maidens = row['M']
        economy = row['Eco']  # Assuming you have an 'Eco' column for economy rate
        player_points = 0
        
        # Points for wickets
        player_points += wickets  # 1 point per wicket
        if wickets >= 3:
            player_points += 5  # Additional 5 points for 3 wickets
        if wickets >= 5:
            player_points += 10  # Additional 10 points for 5 wickets
        
        # Points for maidens
        player_points += maidens * 5  # 5 points for each maiden
        
        # Points for economy
        if economy <= 3:
            player_points += 2  # 2 points for economy <= 3
        if economy > 8:
            player_points += 2  # 2 points for economy > 8
        
        points_per_match.append(player_points)
    
    return points_per_match



st.set_page_config(
    page_title="Analyzer by Crickonnect",
    page_icon="🏏", 
    layout="wide" 
)






# Get the absolute path to the assets directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
image_path = os.path.join(parent_dir, "assets", "ybcclogo.jpg")

# Create columns for logo and title
col1, col2 = st.columns([1, 6])
with col1:
    st.image(image_path, width=60)
with col2:
    st.markdown("<h1 style='color: black; font-size:36px; margin-top: 10px;'>Young Blood Cricket Club</h1>", unsafe_allow_html=True)
# st.subheader("Insights That Sharpen the Edge")



st.markdown(
    """
    <style>
    /* Sidebar background with blur effect */
    .stSidebar {
        min-width: 300px !important;
        max-width: 300px !important;
        background-color: black;  /* Semi-transparent background */
  
    }

    /* Set the font color to white for the sidebar content */
    .stSidebar .sidebar-content {
        color: white;  /* Text color */
    }

    /* Set the title (h1) color to white inside the sidebar */
    .stSidebar h1 {
        color: white !important;  /* Title color in the sidebar */
        font-size: 32px !important;
        padding-bottom: 0px !important;
    }

    /* Set the color of markdown text */
    .stSidebar .stMarkdown {
        color: white !important;  /* Markdown text color */
    }

    /* Sidebar button color */
    .stSidebar .stButton button {
        background-color: #FF5733;  /* Button background color */
        color: white;  /* Button text color */
        border-radius: 5px;  /* Rounded corners for buttons */
        padding: 10px;
    }
    .st-emotion-cache-1mw54nq p{
        color: red;
    }
    /* Sidebar file uploader button color */
    .stSidebar .stFileUploader input[type='file'] {
        background-color: #FF5733;  /* Customize file upload button color */
        color: white;  /* File upload button text color */
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .st-emotion-cache-taue2i {
        background-color: #000000 !important;
        color: #ffffff !important;
        border-radius: 5px;
        padding: 20px 40px !important;
        border: 1px solid white;
    }
    .st-emotion-cache-zaw6nw {
        color: black !important;
        border-radius: 4px !important;
        width: 150px !important;
        margin-top: 8px !important;
    }
    .st-emotion-cache-zaw6nw:hover {
        background-color: white !important;
        color: black !important;
        border: 1px solid black !important;
    }
    .st-emotion-cache-1aehpvj {
        color: white !important;
    }
    .st-emotion-cache-1v45yng .es2srfl9 {
        color: white !important;
    }
    .st-emotion-cache-qsoh6x {
        box-shadow: rgba(0, 0, 0, 0.16) 0px 3px 6px, rgba(0, 0, 0, 0.23) 0px 3px 6px !important;
        fill: black !important;
        background-color: white !important;
        border: 1px solid white !important;
        border-radius: 40px !important;
    }
    # .st-c8 {
    #     box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px !important;
    # }
    .st-emotion-cache-ocsh0s {
        margin-top: 50px !important;
        width: 340px !important;
        height: 50px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


with st.sidebar:
    st.title("Crickonnect")
    st.write("Knock 'em out!")
    
    # Google Sheets Configuration
    SHEET_ID = "1hqTg8XVzCIbXgsq2fmZoN1ffv2-hOdtD3SPJoE64lA0"
    SHEET_NAME = "Ybccdata"
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

    @st.cache_data(ttl="5m")  # Refresh every 5 minutes
    def load_data():
        try:
            return pd.read_csv(url)
        except Exception as e:
            st.error(f"Error loading data: {str(e)}")
            return None

    # Add refresh button
    if st.button("🔄 Refresh Data", key="refresh-button"):
        st.cache_data.clear()
        st.rerun()

    # Load data
    data = load_data()

    # Data load status
    if data is not None:
        st.success("Data loaded successfully!")
    else:
        st.error("Unable to load data. Please check the connection.")

# Check if file is uploaded
if data is not None:
    # Load data
    

    # Player selection
    players = data['Player'].unique()
    player_choice = st.selectbox("Select a Player", players)

    # Filter data for the selected player
    player_data = data[data['Player'] == player_choice]

    # Player-specific stats container
    st.markdown(f"""
        <div class="stats-container">
            <div class="stats-header">
                <h3>{player_choice}</h3>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Batting stats
    if not player_data.empty:
        total_runs = player_data['Runs'].sum()
        total_innings = len(player_data)
        batting_avg = round(total_runs / total_innings, 2) if total_innings > 0 else 0

        st.markdown(
            f'<p class="small-subheader">Played {len(player_data)} Matches</p>', 
            unsafe_allow_html=True
        )
    else:
        st.warning(f"No data available for {player_choice}.")
else:
    st.info("Upload a file to view player data.")

# Apply custom styles globally
st.markdown("""
<style>
    .small-subheader {
        font-size: 16px; 
        font-weight: bold; 
        color: #333; 
    }
</style>
""", unsafe_allow_html=True)

# Stats expander section
if data is not None and not player_data.empty:
    with st.expander("Stats", expanded=True):
        # Batting performance
        points_per_match = calculate_batsman_points_per_match(player_data)
        average_points_per_match = (
            sum(points_per_match) / len(points_per_match) if points_per_match else 0
        )
        total_points = calculate_total_batsman_points(player_data)

        st.markdown(
            f"<h3 style='font-size: 18px; color: #27ae60;'>With the bat</h3>"
            f"<p style='font-size: 16px; color: #27ae60;'>Total Points: {total_points}</p>",
            unsafe_allow_html=True,
        )

        # Display batting stats in columns
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        heading_font_size = "16px"
        stat_font_size = "26px"

        with col1:
            st.markdown(
                f'<p style="font-size: {heading_font_size}; color: #555;">Runs</p>'
                f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["Runs"].sum():,.0f}</p>',
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f'<p style="font-size: {heading_font_size}; color: #555;">Balls</p>'
                f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["Balls"].sum():,.0f}</p>',
                unsafe_allow_html=True,
            )
        with col3:
            st.markdown(
                f'<p style="font-size: {heading_font_size}; color: #555;">Average</p>'
                f'<p style="font-size: {stat_font_size}; color: #000;">{batting_avg}</p>',
                unsafe_allow_html=True,
            )
        with col4:
            st.markdown(
                f'<p style="font-size: {heading_font_size}; color: #555;">Strike Rate</p>'
                f'<p style="font-size: {stat_font_size}; color: #000;">{round(player_data["SR"].mean(), 2)}</p>',
                unsafe_allow_html=True,
            )
        with col5:
            st.markdown(
                f'<p style="font-size: {heading_font_size}; color: #555;">4s</p>'
                f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["4s"].sum():,.0f}</p>',
                unsafe_allow_html=True,
            )
        with col6:
            st.markdown(
                f'<p style="font-size: {heading_font_size}; color: #555;">6s</p>'
                f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["6s"].sum():,.0f}</p>',
                unsafe_allow_html=True,
            )
        with col7:
            st.markdown(
                f'<p style="font-size: {heading_font_size}; color: #555;">High Score</p>'
                f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["Runs"].max():,.0f}</p>',
                unsafe_allow_html=True,
            )

        st.markdown("---")

        # Bowling Performance
        if player_data["O"].sum() > 0:
            st.markdown(
                "<h3 style='font-size: 18px; color: #27ae60;'>With the ball</h3>",
                unsafe_allow_html=True,
            )

            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

            with col1:
                st.markdown(
                    f'<p style="font-size: {heading_font_size}; color: #555;">Total Overs</p>'
                    f'<p style="font-size: {stat_font_size}; color: #000;">{round(player_data["O"].sum(), 2)}</p>',
                    unsafe_allow_html=True,
                )
            with col2:
                st.markdown(
                    f'<p style="font-size: {heading_font_size}; color: #555;">Dot Balls</p>'
                    f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["0s"].sum():,.0f}</p>',
                    unsafe_allow_html=True,
                )
            with col3:
                st.markdown(
                    f'<p style="font-size: {heading_font_size}; color: #555;">Maidens</p>'
                    f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["M"].sum():,.0f}</p>',
                    unsafe_allow_html=True,
                )
            with col4:
                st.markdown(
                    f'<p style="font-size: {heading_font_size}; color: #555;">Runs</p>'
                    f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["R"].sum():,.0f}</p>',
                    unsafe_allow_html=True,
                )
            with col5:
                st.markdown(
                    f'<p style="font-size: {heading_font_size}; color: #555;">Wickets</p>'
                    f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["W"].sum():,.0f}</p>',
                    unsafe_allow_html=True,
                )
            with col6:
                st.markdown(
                    f'<p style="font-size: {heading_font_size}; color: #555;">Economy</p>'
                    f'<p style="font-size: {stat_font_size}; color: #000;">{round(player_data["Eco"].mean(), 2)}</p>',
                    unsafe_allow_html=True,
                )
            with col7:
                st.markdown(
                    f'<p style="font-size: {heading_font_size}; color: #555;">Wides</p>'
                    f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["WD"].sum():,.0f}</p>',
                    unsafe_allow_html=True,
                )
            with col8:
                st.markdown(
                    f'<p style="font-size: {heading_font_size}; color: #555;">No Balls</p>'
                    f'<p style="font-size: {stat_font_size}; color: #000;">{player_data["NB"].sum():,.0f}</p>',
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                "<p style='font-size: 16px; color: #555;'>This player has not bowled in any match.</p>",
                unsafe_allow_html=True,
            )



    
col1, col2, col3 = st.columns(3) 

with col1:
    batting_button = st.button("Batting Analysis")

with col2:
    bowling_button = st.button("Bowling Analysis")

with col3:
    team_analysis = st.button("Team Analysis")



# Batting Analysis
# Batting Analysis
if batting_button:
 
    player_data = data[data['Player'] == player_choice]

    # 1. Runs Scored per Match
    fig = go.Figure()

    match_numbers = list(range(1, len(player_data) + 1))  # Create integer match numbers

    # Add Bar trace for Runs
    fig.add_trace(
        go.Bar(
            x=match_numbers,  # Match numbers on x-axis
            y=player_data['Runs'],  # Runs scored in each match
            name="Runs",
            hovertemplate="Match: %{x}<br>Runs: %{y}<extra></extra>",
            marker_color='#2980b9'  # Bar color
        )
    )

    # Update layout for the bar chart
    fig.update_layout(
        title=f'Runs Scored by {player_choice}',
        xaxis_title="Match",
        yaxis_title="Runs",
        hovermode='x unified',
        xaxis=dict(tickmode='linear', tick0=1, dtick=1)  # Force integer ticks
        
    )

    # Show the plot
    st.plotly_chart(fig)

    # 2. Points Earned per Match
    points_per_match = calculate_batsman_points_per_match(player_data)

    fig_points = go.Figure()

    # Add Bar trace for Points
    fig_points.add_trace(
        go.Bar(
            x=match_numbers,  # Match numbers on x-axis
            y=points_per_match,  # Points earned in each match
            name="Points",
            hovertemplate="Match: %{x}<br>Points: %{y}<extra></extra>",
            marker_color='orange'  # Bar color for points
        )
    )

    # Update layout for the points bar chart
    fig_points.update_layout(
        title=f'Points Earned by {player_choice} per Match',
        xaxis_title="Match",
        yaxis_title="Points",
        hovermode='x unified',
        xaxis=dict(tickmode='linear', tick0=1, dtick=1)  # Force integer ticks
    )

    # Show the points plot
    st.plotly_chart(fig_points)

    # 3. Strike Rate Trend
    fig_sr = go.Figure()
    fig_sr.add_trace(
        go.Scatter(
            x=match_numbers,  # Use integer match numbers
            y=player_data['SR'],
            fill='tozeroy',
            name="Strike Rate",
            hovertemplate="Match: %{x}<br>Strike Rate: %{y:.2f}<extra></extra>",  # Format match as integer
            line=dict(color='green', width=2),
            mode='lines+markers'
        )
    )

    fig_sr.update_layout(
        title=f'Strike Rate Progression of {player_choice}',
        xaxis_title="Match",
        yaxis_title="Strike Rate",
        hovermode='x unified',
        xaxis=dict(
            tickmode='array',
            ticktext=match_numbers,  # Set tick labels as integers
            tickvals=match_numbers,  # Set tick values as integers
            dtick=1  # Force spacing of 1
        )
    )
    st.plotly_chart(fig_sr)

    # 4. Boundary Analysis
    total_runs = player_data['Runs'].sum()
    runs_from_fours = player_data['4s'].sum() * 4
    runs_from_sixes = player_data['6s'].sum() * 6
    other_runs = total_runs - (runs_from_fours + runs_from_sixes)

    fig_boundary = go.Figure(data=[go.Bar(
        x=['Runs from 4s', 'Runs from 6s', 'Other Runs'],
        y=[runs_from_fours, runs_from_sixes, other_runs],
        text=[f'{(runs_from_fours/total_runs)*100:.1f}%', 
              f'{(runs_from_sixes/total_runs)*100:.1f}%', 
              f'{(other_runs/total_runs)*100:.1f}%'],
        textposition='auto',
        hovertemplate="Type: %{x}<br>Runs: %{y}<br>Percentage: %{text}<extra></extra>",
        marker_color=['#c0392b', '#2980b9', '#27ae60']
    )])

    fig_boundary.update_layout(
        title=f'Run Distribution for {player_choice}',
        xaxis_title="Run Type",
        yaxis_title="Runs"
    )
    st.plotly_chart(fig_boundary)

    # 4. Batting Impact Analysis
    fig = go.Figure()
    match_numbers = list(range(1, len(player_data) + 1))  # Create integer match numbers
    
    fig.add_trace(
        go.Scatter(
            x=player_data['SR'],
            y=player_data['Runs'],
            mode='markers',
            marker=dict(
                size=12,
                color=match_numbers,  
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(
                    title="Match Number",
                    tickmode='array',
                    ticktext=match_numbers,  # Set tick labels as integers
                    tickvals=match_numbers,  # Set tick values as integers
                )
            ),
            hovertemplate="Match: %{marker.color:.0f}<br>Strike Rate: %{x:.2f}<br>Runs: %{y}<extra></extra>"  # Format match number as integer
        )
    )
    
    fig.update_layout(
        title=f'Batting Impact: Runs vs Strike Rate for {player_choice}',
        xaxis_title="Strike Rate",
        yaxis_title="Runs Scored"
    )
    st.plotly_chart(fig)




if bowling_button:
    # Filter data for the selected player
    player_data = data[data['Player'] == player_choice]

    # Check if player has bowled more than 3 overs
    total_overs = player_data['O'].sum()
    
    if total_overs >= 3:
        # 1. Wickets per Match Chart
        fig_wickets = go.Figure()
        fig_wickets.add_trace(
            go.Bar(x=player_data['Match'], 
                  y=player_data['W'],
                  name='Wickets',
                  marker_color='#2980b9')
        )
        fig_wickets.update_layout(
            height=400,
            title=f"{player_choice}'s Wickets per Match Analysis",
            xaxis_title="Match Number",
            yaxis_title="Wickets Taken",
            title_x=0,
            xaxis=dict(
                tickmode='linear',
                tick0=1,
                dtick=1  # Show whole numbers for matches
            ),
            yaxis=dict(
                tickmode='linear',
                tick0=0,
                dtick=1  # Show whole numbers for wickets
            ), 
           bargroupgap=0.1
        )
        st.plotly_chart(fig_wickets, use_container_width=True)

        # 2. Economy Rate Trend
        fig_economy = go.Figure()
        fig_economy.add_trace(
            go.Scatter(x=player_data['Match'], 
                   y=player_data['Eco'],
                   name='Economy',
                   line=dict(color='#2ca02c'))
        )
        fig_economy.update_layout(
            height=400,
            title=f"{player_choice}'s Economy Rate Trend",
            xaxis_title="Match Number",
            yaxis_title="Economy Rate",
            title_x=0,
            xaxis=dict(
                tickmode='linear',
                tick0=1,
                dtick=1  # Show whole numbers for matches
            )
        )
        st.plotly_chart(fig_economy, use_container_width=True)

        # 3. Points Earned per Match
        bowler_points_per_match = calculate_bowler_points_per_match(player_data)

        fig_bowler_points = go.Figure(data=[go.Bar(
            x=player_data['Match'],  # Match numbers on x-axis
            y=bowler_points_per_match,
            text=bowler_points_per_match,
            textposition='auto',
            name='Points',
            marker_color='orange'  # Bar color for points
        )])
        
        fig_bowler_points.update_layout(
            height=400,
            title=f"{player_choice}'s Points Earned per Match",
            xaxis_title="Match Number",
            yaxis_title="Points",
            title_x=0,
            xaxis=dict(
                tickmode='linear',
                tick0=1,
                dtick=1  # Show whole numbers for matches
            )
        )
        st.plotly_chart(fig_bowler_points, use_container_width=True)



        # 3. Runs Conceded Breakdown
        fig_pie = go.Figure(data=[go.Pie(
            labels=['Dot Balls', 'Runs', 'Extras'],
            values=[player_data['0s'].sum(), 
                   player_data['R'].sum() - (player_data['WD'].sum() + player_data['NB'].sum()),
                   player_data['WD'].sum() + player_data['NB'].sum()],
            hole=.3,
            marker_colors=['#40739e', '#2f3640', '#d62728']
        )])
        fig_pie.update_layout(
            height=400,
            title=f"{player_choice}'s Runs Conceded Analysis",
            title_x=0  # Left align title
        )
        st.plotly_chart(fig_pie, use_container_width=True)

        # 4. Bowling Performance Summary
        fig_summary = go.Figure(data=[go.Bar(
            x=['Total Wickets', 'Maidens', 'Economy'],
            y=[player_data['W'].sum(), 
               player_data['M'].sum(), 
               round(player_data['Eco'].mean(), 2)],
            marker_color=['#006266', '#009432', '#A3CB38']
        )])
        fig_summary.update_layout(
            height=400,
            title=f"{player_choice}'s Bowling Performance Summary",
            title_x=0,  # Left align title
            bargroupgap=0.1 
        )
        st.plotly_chart(fig_summary, use_container_width=True)

    else:
        st.info(f"No detailed bowling analysis available for {player_choice} (Less than 3 overs bowled)")


if team_analysis:

    # 5. Overall Team Performance
    # st.subheader("Overall Team Performance")
    # st.write("#### Runs Scored by All Players")
    
    team_runs = data.groupby('Player')['Runs'].sum().sort_values(ascending=False)
    
    fig = go.Figure(data=[
        go.Bar(
            x=team_runs.index,
            y=team_runs.values,
            text=team_runs.values,
            textposition='auto',
            hovertemplate="Player: %{x}<br>Total Runs: %{y}<extra></extra>",
            marker_color='red'
        )
    ])
    
    fig.update_layout(
        title='Total Runs Scored by Each Player',
        xaxis_title="Player",
        yaxis_title="Total Runs",
        bargap=0.3,
        bargroupgap=0.10
    )
    st.plotly_chart(fig)

    # After all individual player analysis, add total wickets comparison
    # st.write("### Team Bowling Analysis")
    # st.subheader("Wickets Taken by All Players")

    # Group by Player and sum their wickets
    wickets_by_player = data.groupby('Player')['W'].sum().sort_values(ascending=False)

    # Create bar chart for wickets comparison
    fig_team_wickets = go.Figure()
    fig_team_wickets.add_trace(
        go.Bar(
            x=wickets_by_player.index,
            y=wickets_by_player.values,
            marker_color='#1f77b4',  
            text=wickets_by_player.values,  
            textposition='auto',  
        )
    )

    # Update layout
    fig_team_wickets.update_layout(
        title='Total Wickets Taken by Each Player',
        xaxis_title="Players",
        yaxis_title="Total Wickets",
        showlegend=False,
        bargap=0.3,
        bargroupgap=0.10,  
    )

    # Show the figure
    st.plotly_chart(fig_team_wickets)


