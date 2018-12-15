import {
    GET_BOARD,
} from "../actions/types";


const initialState = {
    board: Array(9).fill(0),
    player: '',
    computer: '',
};

export default function(state = initialState, action) {
    switch(action.type) {
        case GET_BOARD:
            return { board: action.payload };
        default:
            return state;
    }
}
