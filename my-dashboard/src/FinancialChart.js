import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import SearchBar from './SearchBar';

class FinancialChart extends React.Component {
    constructor(props) {
        super(props);
        this.state = { data: [], symbol: '' };
    }

    handleSearch = (symbol) => {
        fetch(`http://localhost:5000/${symbol}/history/1y`)
            .then(response => response.json())
            .then(rawData => {
                const processedData = Object.keys(rawData.Open).map(timestamp => {
                    return {
                        date: new Date(parseInt(timestamp)).toLocaleDateString("en-US"),
                        open: rawData.Open[timestamp],
                        high: rawData.High[timestamp],
                        low: rawData.Low[timestamp],
                        close: rawData.Close[timestamp],
                        volume: rawData.Volume[timestamp]
                    };
                });
                this.setState({ data: processedData, symbol: symbol });
            })
            .catch(error => {
                console.error('Error fetching historical data:', error);
            });
    };
    render() {
        return (
            <div className="container sample">
                <SearchBar onSearch={this.handleSearch} />
                <div className="container" style={{ height: "calc(100% - 25px)" }}>
                <LineChart width={1600} height={700} data={this.state.data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="date" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="open" stroke="#8884d8" activeDot={{ r: 8 }} />
                    <Line type="monotone" dataKey="close" stroke="#82ca9d" />
                </LineChart>
                </div>
            </div>
        );
    }
}

export default FinancialChart;
