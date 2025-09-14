function CurrentDate() {
  const date = new Date();
  const day = date.getDay();
  const weekday = day >= 1 && day <= 5;
  return (
    <h2>
      Today's date is: {date.toLocaleDateString()} and it's a{" "}
      {weekday ? "weekday" : "weekend"}.
    </h2>
  );
}

function Homepage() {
  return (
    <div>
      <h1>Welcome to the Homepage</h1>
      <CurrentDate />
    </div>
  );
}

export default Homepage;
