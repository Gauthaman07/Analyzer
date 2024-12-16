import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load Data
st.title("Young Blood Cricket Club")
st.subheader("Insights That Sharpen the Edge")
st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Batting Performance
    st.subheader("Player Performance - Batting")
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
                <h3>{player_choice}'s Batting Performance</h3>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Calculate total statistics in the dark container
    total_stats = {
        "Matches Played": len(player_data),
        "Total Runs": player_data['Runs'].sum(),
        "Total Balls": player_data['Balls'].sum(),
        "Average Strike Rate": round(player_data['SR'].mean(), 2),
        "Total Fours": player_data['4s'].sum(),
        "Total Sixes": player_data['6s'].sum()
    }
    
    # Display metrics in columns (these will inherit the dark background)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Matches Played", total_stats["Matches Played"])
        st.metric("Total Runs", total_stats["Total Runs"])
    with col2:
        st.metric("Total Balls", total_stats["Total Balls"])
        st.metric("Average Strike Rate", total_stats["Average Strike Rate"])
    with col3:
        st.metric("Total Fours", total_stats["Total Fours"])
        st.metric("Total Sixes", total_stats["Total Sixes"])

    # 1. Runs per Match
    st.write("#### Runs Scored in Each Match")
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
    
    # Add Line chart
    fig.add_trace(
        go.Scatter(
            x=match_numbers,  # Use integer match numbers
            y=player_data['Runs'],
            name="Runs Trend",
            hovertemplate="Match: %{x}<br>Runs: %{y}<extra></extra>",
            line=dict(color='navy', width=2),
            mode='lines+markers'
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
    st.write("#### Strike Rate Progression")
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
    st.write("#### Boundary Analysis")
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
    st.write("#### Batting Impact Analysis")
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

    # 5. Overall Team Performance
    st.subheader("Overall Team Performance")
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

else:
    st.write("Please upload a CSV file to start analyzing!")