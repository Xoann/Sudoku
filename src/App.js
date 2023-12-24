import Sudoku from "./Sudoku";
import './App.css';
import {useEffect, useState} from "react";
import io from 'socket.io-client';
import tile from "./Tile";
import Dropdown from "./Dropdown";

let socket = io('http://localhost:5000/solve')

function App() {
    const size = 3
    const [boardState, setBoardState] = useState(Array(size ** 4).fill(''))
    const [validBoard, setValidBoard] = useState(null)
    const [algorithm, setAlgorithm] = useState('backtrack')

    const handleBoardStateChange = (newState) => {
        setBoardState(newState)
    }

    const handleAlgorithmChange = (newAlgo) => {
        setAlgorithm(newAlgo)
    }

    const sendBoardToValidate = async (data) => {
        try {
            const response = await fetch('http://localhost:5000/validate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });

            // if (!response.ok) {
            //     throw new Error('Network response was not ok');
            // }

            const result = await response.json();
            setValidBoard(result.result);
        } catch (error) {
            console.error("There was a problem with the fetch operation", error)
        }
    }

    useEffect(() => {
        socket.on('board_update', (data) => {
            // console.log(data.board)
            setBoardState(data.board)
        });

        return () => {
            socket.disconnect();
        }
    }, []);

    const handleSolveClick = () => {
        socket.connect()
        socket.emit('solve', boardState, algorithm)
    }

    const handleClearClick = () => {
        const emptyBoard = Array(size ** 4).fill('')
        setBoardState(emptyBoard)
    }



  return (
    <div className="app">
      <Sudoku
        updateBoardState={handleBoardStateChange}
        boardUpdate={boardState}
      />
        <div className={"buttons"}>
            <div
                onClick={() => sendBoardToValidate(boardState)}
                className={`btn validate-button ${validBoard === false ? 'invalid' : validBoard === null ? '' : 'valid'}`}>
                <span>Validate</span>
                <span className={`valid-notice notice`}>Valid</span>
                <span className={`invalid-notice notice`}>Invalid</span>
            </div>
            <div className={"btn generate-button"}>
                <span>Generate</span>
            </div>
            <Dropdown
                setAlgo={handleAlgorithmChange}
            />
            <div
                onClick={handleSolveClick}
                className={"btn solve-button"}>
                <span>Solve</span>
            </div>
            <div
                onClick={handleClearClick}
                className={"btn clear-button"}>
                <span>Clear</span>
            </div>
        </div>
    </div>
  );
}

export default App;
