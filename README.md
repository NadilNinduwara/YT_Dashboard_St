This project aims to provide a comprehensive YouTube dashboard for analyzing and visualizing aggregated metrics and individual video performance. It utilizes machine learning and data science techniques to extract insights from YouTube data.

Prerequisites
To run this project, the following libraries need to be installed using pip:

pandas
numpy
plotly
streamlit

Usage
Clone the repository to your local machine.
Open a Python IDE or terminal and navigate to the project directory.
Install the required libraries listed above.
Ensure that the necessary data files are present in the project directory, including:
Aggregated_Metrics_By_Video.csv
Aggregated_Metrics_By_Country_And_Subscriber_Status.csv
Video_Performance_Over_Time.csv
Run the provided code to launch the YouTube dashboard.
The dashboard provides two options:
Aggregate Metrics: Explore aggregated metrics for the YouTube channel, including views, likes, subscribers, engagement ratio, and more. The dashboard presents key metrics, calculates deltas compared to the previous 6 and 12 months, and visualizes the data.
Individual Video Analysis: Analyze the performance of individual videos. Select a video from the dropdown menu, and the dashboard will display metrics such as views, subscribers, engagement ratio, and a bar chart showing views by country. Additionally, a line chart illustrates the cumulative views of the video over the first 30 days of publication.

Data
The dashboard relies on the following data files:

Aggregated_Metrics_By_Video.csv: Contains aggregated metrics for each video, including views, likes, subscribers, comments, and more.
Aggregated_Metrics_By_Country_And_Subscriber_Status.csv: Provides aggregated metrics for each country and subscriber status (subscribed or not) for each video.
Video_Performance_Over_Time.csv: Contains daily video performance data, including views, likes, and comments over time.
Please ensure that these data files are present in the project directory for the dashboard to function properly.

Results
The YouTube dashboard offers a user-friendly interface to explore and analyze YouTube channel metrics. It provides insights into overall channel performance and allows in-depth analysis of individual videos. The visualizations and metrics facilitate understanding and decision-making regarding content creation, audience engagement, and video performance.

Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.

Acknowledgments
This project leverages the power of pandas, NumPy, Plotly, and Streamlit libraries to create an interactive YouTube dashboard. It combines machine learning and data science techniques to provide valuable insights for content creators and YouTube channel managers.

References
pandas Documentation
NumPy Documentation
Plotly Documentation
Streamlit Documentation
