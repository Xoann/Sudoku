import "./Tile.css"

function Tile({ isSelected, onClick, value }) {

    return (<div
        className={`tile ${isSelected ? 'selected' : ''}`}
        onClick={onClick}>
        <span className={"number"}>{value}</span>
    </div>)
}

export default Tile