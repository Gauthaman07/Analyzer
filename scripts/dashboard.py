import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


    # Add custom CSS with more specific selectors
st.markdown("""
        <style>
        /* Metric value styling */
        [data-testid="stMetricValue"] {
            font-size: 24px !important;
            margin-top: 10px !important;
        }
        
        /* Metric label styling */
        [data-testid="stMetricLabel"] {
            font-size: 16px !important;
            font-weight: 600 !important;  /* Try different weight */
        }

        /* Additional selectors for label */
        div[data-testid="stMetricLabel"] > div {
            font-weight: bold !important;
        }
        
        .css-1wivap2 {  /* Additional class for metric label */
            font-weight: bold !important;
        }
        
        [data-testid="stMetricLabel"] p {
            font-weight: bold !important;
        }
        </style>
    """, unsafe_allow_html=True)


# Load Data
st.title("Young Blood Cricket Club")
st.subheader("Insights That Sharpen the Edge")
st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Batting Performance
    # st.subheader("Player Performance - Batting")
    players = data['Player'].unique()
    player_choice = st.selectbox("Select a Player", players)

    # Filter data for the selected player
    player_data = data[data['Player'] == player_choice]
    # Add custom CSS for dark background
    st.markdown(
        """
        <style>
        .stats-container {
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0px;
        }
        .stats-header {
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 15px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Wrap the content in the styled container
    st.markdown(f"""
        <div class="stats-container">
            <div class="stats-header">
                <h3>{player_choice}</h3>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    
    
    # Calculate batting average
    total_runs = player_data['Runs'].sum()
    total_innings = len(player_data)  # or use player_data['Out'].sum() if you have 'Out' column
    batting_avg = round(total_runs / total_innings, 2) if total_innings > 0 else 0



    # Batting Stats in one line
 
    with st.expander("Batting Performance", expanded=True):
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.metric("Matches", len(player_data))
        with col2:
            st.metric("Runs", player_data['Runs'].sum())
        with col3:
            st.metric("Balls", player_data['Balls'].sum())
        with col4:
            st.metric("Average", round(player_data['Runs'].sum() / len(player_data), 2))
        with col5:
            st.metric("Strike Rate", round(player_data['SR'].mean(), 2))
        with col6:
            st.metric("4s", player_data['4s'].sum())
        with col7:
            st.metric("6s", player_data['6s'].sum())

    # Bowling Stats in one line
    with st.expander("Bowling Performance", expanded=True):
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        st.metric("Dot Balls", player_data['0s'].sum())
    with col2:
        st.metric("Maidens", player_data['M'].sum())
    with col3:
        st.metric("Runs", player_data['R'].sum())
    with col4:
        st.metric("Wickets", player_data['W'].sum())
    with col5:
        st.metric("Economy", round(player_data['Eco'].mean(), 2))
    with col6:
        st.metric("Wides", player_data['WD'].sum())
    with col7:
        st.metric("No Balls", player_data['NB'].sum())

    # 1. Runs per Match
    # st.write("#### Runs Scored in Each Match")
    fig = go.Figure()
    
    match_numbers = list(range(1, len(player_data) + 1))  # Create integer match numbers
    
    # Add Bar chart
    fig.add_trace(
        go.Bar(
            x=match_numbers,  # Use integer match numbers
            y=player_data['Runs'],
            name="Runs",
            hovertemplate="Match: %{x}<br>Runs: %{y}<extra></extra>",
            opacity=0.3,
            marker_color='skyblue'
        )
    )

    
    fig.update_layout(
        title=f'Runs Scored by {player_choice}',
        xaxis_title="Match",
        yaxis_title="Runs",
        hovermode='x unified',
        xaxis=dict(tickmode='linear', tick0=1, dtick=1)  # Force integer ticks
    )
    st.plotly_chart(fig)

    # 2. Strike Rate Trend
    # st.write("#### Strike Rate Progression")
    fig = go.Figure()
    
    match_numbers = list(range(1, len(player_data) + 1))  # Create integer match numbers
    
    fig.add_trace(
        go.Scatter(
            x=match_numbers,  # Use integer match numbers
            y=player_data['SR'],
            fill='tozeroy',
            name="Strike Rate",
            hovertemplate="Match: %{x:.0f}<br>Strike Rate: %{y:.2f}<extra></extra>",  # Format match as integer
            line=dict(color='green', width=2),
            mode='lines+markers'
        )
    )
    
    fig.update_layout(
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
    st.plotly_chart(fig)

    # 3. Boundary Analysis
    # st.write("#### Boundary Analysis")
    total_runs = player_data['Runs'].sum()
    runs_from_fours = player_data['4s'].sum() * 4
    runs_from_sixes = player_data['6s'].sum() * 6
    other_runs = total_runs - (runs_from_fours + runs_from_sixes)
    
    fig = go.Figure(data=[
        go.Bar(
            x=['Runs from 4s', 'Runs from 6s', 'Other Runs'],
            y=[runs_from_fours, runs_from_sixes, other_runs],
            text=[f'{(runs_from_fours/total_runs)*100:.1f}%', 
                  f'{(runs_from_sixes/total_runs)*100:.1f}%', 
                  f'{(other_runs/total_runs)*100:.1f}%'],
            textposition='auto',
            hovertemplate="Type: %{x}<br>Runs: %{y}<br>Percentage: %{text}<extra></extra>",
            marker_color=['#FF9999', '#66B2FF', '#99FF99']
        )
    ])
    
    fig.update_layout(
        title=f'Run Distribution for {player_choice}',
        xaxis_title="Run Type",
        yaxis_title="Runs"
    )
    st.plotly_chart(fig)

    # 4. Batting Impact Analysis
    # st.write("#### Batting Impact Analysis")
    fig = go.Figure()
    
    match_numbers = list(range(1, len(player_data) + 1))  # Create integer match numbers
    
    fig.add_trace(
        go.Scatter(
            x=player_data['SR'],
            y=player_data['Runs'],
            mode='markers',
            marker=dict(
                size=12,
                color=match_numbers,  # Use integer match numbers
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





    # Check if player has bowled more than 3 overs
    total_overs = player_data['O'].sum()
    
    if total_overs >= 3:
        # 1. Wickets per Match Chart
        fig_wickets = go.Figure()
        fig_wickets.add_trace(
            go.Bar(x=player_data['Match'], 
                  y=player_data['W'],
                  name='Wickets',
                  marker_color='#1f77b4')
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
            )
        )
        st.plotly_chart(fig_wickets, use_container_width=True)

        # 2. Economy Rate Trend
        fig_economy = go.Figure()
        fig_economy.add_trace(
            go.Line(x=player_data['Match'], 
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

        # 3. Runs Conceded Breakdown
        fig_pie = go.Figure(data=[go.Pie(
            labels=['Dot Balls', 'Runs', 'Extras'],
            values=[player_data['0s'].sum(), 
                   player_data['R'].sum() - (player_data['WD'].sum() + player_data['NB'].sum()),
                   player_data['WD'].sum() + player_data['NB'].sum()],
            hole=.3,
            marker_colors=['#ff7f0e', '#1f77b4', '#d62728']
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
            marker_color=['#1f77b4', '#2ca02c', '#ff7f0e']
        )])
        fig_summary.update_layout(
            height=400,
            title=f"{player_choice}'s Bowling Performance Summary",
            title_x=0  # Left align title
        )
        st.plotly_chart(fig_summary, use_container_width=True)




    else:
        st.info(f"No detailed bowling analysis available for {player_choice} (Less than 3 overs bowled)")


    # 5. Overall Team Performance
    # st.subheader("Overall Team Performance")
    st.write("#### Runs Scored by All Players")
    
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
        xaxis_tickangle=45
    )
    st.plotly_chart(fig)

    # After all individual player analysis, add total wickets comparison
    st.write("### Team Bowling Analysis")
    st.subheader("Wickets Taken by All Players")

    # Group by Player and sum their wickets
    wickets_by_player = data.groupby('Player')['W'].sum().sort_values(ascending=False)

    # Create bar chart for wickets comparison
    fig_team_wickets = go.Figure()
    fig_team_wickets.add_trace(
        go.Bar(
            x=wickets_by_player.index,
            y=wickets_by_player.values,
            marker_color='#1f77b4',  # Blue color
            text=wickets_by_player.values,  # Add value labels
            textposition='auto',  # Show labels on bars
        )
    )

    # Update layout
    fig_team_wickets.update_layout(
        height=400,
        xaxis_title="Players",
        yaxis_title="Total Wickets",
        showlegend=False,
        xaxis_tickangle=-45,  # Angle player names for better readability
        margin=dict(b=100),  # Add bottom margin for rotated labels
        yaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=1  # Show whole numbers for wickets
        )
    )

    # Show the figure
    st.plotly_chart(fig_team_wickets, use_container_width=True)

    # Optional: Add a data table below the chart
    # st.write("Wickets Breakdown")
    # wickets_df = wickets_by_player.reset_index()
    # wickets_df.columns = ['Player', 'Total Wickets']
    # st.dataframe(wickets_df, hide_index=True)


else:
    st.write("Please upload a CSV file to start analyzing!")