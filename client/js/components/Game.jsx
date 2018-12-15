import React, { Component } from "react";
import Board from "./Board";
import { connect } from "react-redux";
import {
    playGetBoard,
} from "../actions/game";

class App extends Component {
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(i) {
        const {
            player,
            computer,
            board
        } = this.props;

        this.props.playGetBoard({
            player: -1,
            computer: 1,
            board,
        }, i);
    }

    render() {
        return (
			<div className="game">
				<div className="game-board">
					<Board
						squares={this.props.board}
						onClick={(i) => this.handleClick(i)}
					/>
				</div>
			</div>
        );
    }
}

function bindAction(dispatch) {
    return {
        playGetBoard: ({player,computer,board}, human) => dispatch(playGetBoard({player,computer,board}, human)),
    }
}
const mapStateToProps = state => ({
    board: state.gameReducer.board,
    player: state.gameReducer.player,
    computer: state.gameReducer.computer,
});

export default connect(mapStateToProps, bindAction)(App);