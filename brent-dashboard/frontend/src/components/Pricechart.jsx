import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, ReferenceLine
} from "recharts";

const PriceChart = () => {
  const [data, setData] = useState([]);
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/price-change-points")
      .then(res => setData(res.data));
    axios.get("http://localhost:5000/api/events")
      .then(res => setEvents(res.data));
  }, []);

  return (
    <LineChart width={900} height={400} data={data}>
      <CartesianGrid stroke="#ccc" />
      <XAxis dataKey="DetectedChangeDate" />
      <YAxis />
      <Tooltip />
      <Line type="monotone" dataKey="LogPrice" stroke="#8884d8" />
      {events.map((e, i) => (
        <ReferenceLine
          key={i}
          x={e.EventDate}
          stroke="red"
          strokeDasharray="3 3"
          label={e.EventName}
        />
      ))}
    </LineChart>
  );
};

export default PriceChart;
