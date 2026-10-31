import streamlit as st
import pandas as pd
import plotly.express as px 


st.title("Cars Dashboard")
st.header("CIS 3590 - Internship-Ready Software Development")

st.divider()

df = pd.read_csv("cars.csv")
labels = {
    "horsepower": "Horsepower",
    "enginesize": "Engine Size",
    "curbweight": "Curb Weight",
    "citympg": "City MPG",
    "highwaympg": "Highway MPG",
    "price": "Price ($)",
    "fueltype": "Fuel Type"
}

st.sidebar.header("Filters")
st.sidebar.info("These filters update the Data, Chart and Insights tabs")

body_styles = ["All"] + sorted(df["carbody"].unique().tolist())
body_style = st.sidebar.selectbox("Select a body style", options=body_styles)

min_price = int(df["price"].min())
max_price = int(df["price"].max())
start, end = st.sidebar.slider(
    "Select a price range",
    min_price,
    max_price,
    (min_price, max_price)
)

filtered_df = df[(df["price"] >= start) & (df["price"] <= end)]
if body_style != "All":
    filtered_df = filtered_df[filtered_df["carbody"] == body_style]

overview, data, chart, insights = st.tabs(["Overview",
                                           "Data",
                                           "Chart",
                                           "Insights"])
with overview:
    st.subheader("Overview")
    st.write("This app explores a dataset of cars. Use it to see how a car's "
             "specifications, such as horsepower, size and fuel economy, "
             "relate to its price.")
    st.write(f"The dataset has {df.shape[0]} cars and {df.shape[1]} columns. "
             "Choose a body style and a price range in the sidebar, then open "
             "the other tabs to see the results.")

with data:
    st.subheader("Data")
    st.write(f"Showing {len(filtered_df)} of {len(df)} cars.")
    if filtered_df.empty:
        st.warning("No cars match these filters. Try a wider price range.")
    else:
        st.dataframe(filtered_df)
        st.caption("Filtered Data")
        st.dataframe(filtered_df.describe())
        st.caption("Descriptive Statistics")

with chart:
    st.subheader("Scatter Plot")
    st.write("Each point is one car. Hover over a point to see its details.")
    parameter = st.selectbox("Select a parameter",
                             options=["horsepower", "enginesize", "curbweight",
                                      "citympg", "highwaympg"],
                             format_func=lambda column: labels[column])
    if filtered_df.empty:
        st.warning("No cars match these filters. Try a wider price range.")
    else:
        fig1 = px.scatter(filtered_df,
                          x=parameter,
                          y="price",
                          color="fueltype",
                          hover_name="CarName",
                          labels=labels,
                          title=f"{labels[parameter]} vs. Price")
        st.plotly_chart(fig1)

with insights:
    st.subheader("Insights")
    if filtered_df.empty:
        st.warning("No cars match these filters. Try a wider price range.")
    else:
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Cars",
            len(filtered_df)
        )

        col2.metric(
            "Average Price",
            f"${filtered_df['price'].mean():,.0f}"
        )

        col3.metric(
            "Average City MPG",
            f"{filtered_df['citympg'].mean():.1f}")

        expensive_car = filtered_df.loc[filtered_df["price"].idxmax()]
        st.write(f"The most expensive car shown is the "
                 f"{expensive_car['CarName']} at ${expensive_car['price']:,.0f}.")

        correlation = filtered_df[parameter].corr(filtered_df["price"])
        if len(filtered_df) < 3 or pd.isna(correlation):
            st.write("There are not enough different cars here to compare "
                     f"{labels[parameter]} and price.")
        else:
            if correlation > 0:
                direction = "tends to rise"
            else:
                direction = "tends to fall"
            st.write(f"For these cars, price {direction} as "
                     f"{labels[parameter]} increases "
                     f"(correlation: {correlation:.2f}).")
            st.caption("A correlation describes a pattern in this data. "
                       "It does not prove that one thing causes the other.")
