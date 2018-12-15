import {
    GET_BOARD
} from "./types";

const SERVER_URL = '';

export const playGetBoard = ({player,computer,board}, human) => dispatch => {
    fetch(SERVER_URL + 'round/' + human, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({
            player: player,
            computer: computer,
            board: board,
        })
    }).then(function(response) { return response.json(); })
        .then(function(data) {
            dispatch({
                type: GET_BOARD,
                payload: data
            });
        })
};