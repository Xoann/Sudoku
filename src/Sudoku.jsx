import Tile from "./Tile";
import "./Sudoku.css"
import {useEffect, useState} from "react";

function Sudoku({ updateBoardState, boardUpdate }) {
    const size = 3
    const sizeArray = Array.from({length: size ** 2}, (_, index) => index);

    const [selectedTile, setSelectedTile] = useState(null);
    const [tileValues, setTileValues] = useState(Array(size ** 4).fill(''));


    const handleTileClick = (index) => {
        setSelectedTile(index === selectedTile ? null : index)
    }

    const handleKeyDown = (event) => {
        const legalValues = Array.from({ length: size ** 2 }, (_, index) => (index + 1).toString());
        if (legalValues.includes(event.key) && selectedTile !== null) {
            const newTileValues = [...tileValues];
            newTileValues[selectedTile] = event.key;
            setTileValues(newTileValues)
            updateBoardState(newTileValues)

        } else if (event.key === "Backspace" && selectedTile !== null) {
            const newTileValues = [...tileValues];
            newTileValues[selectedTile] = "";
            setTileValues(newTileValues)
            updateBoardState(newTileValues)
        }
        if (event.key === 'a') {
            console.log(tileValues)
        }
    }

    useEffect(() => {
        setTileValues(boardUpdate)
    }, [boardUpdate]);

    useEffect(() => {
        window.addEventListener('keydown', handleKeyDown)

        return () => {
            window.addEventListener('keydown', handleKeyDown)
        }
    }, [selectedTile, tileValues]);





    return (
        <div className={"board"}>
            {sizeArray.map((i) => (
                <div key={i} className={"sub-grid"}>
                    {sizeArray.map((j) => (
                        <Tile
                            key={j}
                            className={"tile"}
                            isSelected={i * size ** 2 + j === selectedTile}
                            onClick={() => handleTileClick(i * size ** 2 + j)}
                            value={tileValues[i * size ** 2 + j]}
                        />

                    ))}
                </div>
            ))}
        </div>
    );
}

export default Sudoku