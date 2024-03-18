import React, { useState } from 'react';

function SearchBar({ onSearch }) {
  const [inputValue, setInputValue] = useState('');
  
  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSearch = () => {
    if (inputValue.trim() === "") {
      return;
    }
    fetch(`http://localhost:5000/symbol/${encodeURIComponent(inputValue)}`)
      .then(response => response.json())
      .then(data => {
        if (data.symbol && onSearch) {
          onSearch(data.symbol);
        } else {
          console.error('Symbol not found');
        }
      })
      .catch(error => {
        console.error('Error converting company name to symbol:', error);
      });
  };

  return (
    <div>
      <input
        type="text"
        value={inputValue}
        onChange={handleInputChange}
        placeholder="Enter a company name (e.g., Advanced Micro Devices)"
      />
      <button onClick={handleSearch}>Search</button>
      
      {inputValue && <div>Search Term: {inputValue}</div>}
    </div>
  );
}

export default SearchBar;
