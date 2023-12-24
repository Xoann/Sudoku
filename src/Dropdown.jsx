import React, { useState } from 'react';
import "./Dropdown.css"

const Dropdown = ({ setAlgo }) => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleDropdown = () => {
        setIsOpen(!isOpen);
    };

    const handleButtonClick = (algo) => {
        setAlgo(algo)
    }

    return (
        <div onClick={toggleDropdown} className={`btn algorithms-button dropdown ${isOpen ? 'open' : ''}`}>
            <span>Strategies</span>
                <div className={`dropdown-content ${isOpen ? '' : 'closed'}`}>
                    <div onClick={() => handleButtonClick("backtrack")}>Backtrack</div>
                    <div onClick={() => handleButtonClick("algo 2")}>Algo 2</div>
                    <div onClick={() => handleButtonClick("algo 3")}>Algo 3</div>
                </div>
        </div>
    );
};

export default Dropdown;