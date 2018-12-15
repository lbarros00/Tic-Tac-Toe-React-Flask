### Setting up client-side with React

Create the following file structure:

```sh
	└── client/
		├── css/
		├── dist/
		├── images/
		└── js/
			├── components/
			└── index.jsx
		├── index.html
		├── package.json
		├── README.md
		└── webpack.config.js
```

```sh
$ mkdir client
$ cd client
```

Create a `package.json` with defaults:

```sh
$ npm init -y
```

Install `Webpack` JavaScript module bundler which significantly decreases loading time for webpages:

```sh
$ npm i webpack --save
```

Let's now install `Babel` which compiles JavaScript to browser-compatible JavaScript:

```sh
$ npm i babel-core babel-preset-es2015 babel-preset-react --save-dev
$ npm i babel-loader --save
```

Add property `"babel"` to add `Babel` presets in `package.json`:

```sh
  “babel”: {
    “presets”: [
      “es2015”,
      “react”
    ]
  },
```

Install `React`:

```sh
$ npm i react react-dom --save
```

Create `webpack.config.js`, notice that in module->rules we exclude node_modules/ to ensure Babel doesn't transform any node modules which speeds the babel-loader:

```sh
	const webpack = require('webpack');
	const config = {
		entry:  __dirname + '\\js\\index.jsx',
		output: {
			path: __dirname + '/dist',
			filename: 'bundle.js'
		},
		resolve: {
			extensions: ['.js', '.jsx', '.css']
		},
		module: {
			rules: [
				{
					test: /\.jsx?/,
					exclude: /node_modules/,
					use: 'babel-loader'
				}
			]
		}
	};
	module.exports = config;
```

Now that we have `webpack.config.js`, we can add commands in `package.json` to automatically build and run code:

```sh
  "scripts": {
    "build": "webpack -p --progress --config webpack.config.js",
    "dev-build": "webpack --progress -d --config webpack.config.js",
    "watch": "webpack --progress -d --config webpack.config.js --watch",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
```

To run the client side:

```sh
$ npm run watch
```

### Setting up Redux to communicate with server-side

Follow this file structure within the `js/` directory:

```sh
    └── js/
        └── actions/
            ├── myAction.jsx
            └── types.jsx
        ├── components/
        └── reducers/
            ├── index.jsx
            └── myReducer.jsx
        ├── index.jsx
        ├── store.jsx
        └── Test.jsx
```

Install the following dependencies to use `Redux`:

```sh
$ npm i redux redux-thunk react-redux --save
```

Create `reducers/index.jsx`

```sh
import { combineReducers } from "redux";
import myReducer from "./myReducer";

export default combineReducers({
    myReducer
});
```

Create `reducers/myReducer.jsx`

```sh
import { FETCH } from "../actions/types";

const initialState = {
    myProperty: {}
};

export default function(state = initialState, action) {
    switch(action.type) {
        case FETCH:
            return {
                myProperty: action.payload
            };
        default:
            return state;
    }
}
```

Create `actions/types.jsx`

```sh
export const FETCH = 'FETCH';
```

Create `actions/myAction.jsx`

```sh
import { FETCH } from "./types";

const SERVER_URL = '';

export const myAction = () => dispatch => {
    // check if this is being called
    console.log("happening");
    fetch(SERVER_URL, {
        method: 'GET',
        headers: {
            'content-type': 'json',
            'Access-Control-Allow-Origin': '*'
        },
    })
        .then(res => res.json())
        .then(data =>
            dispatch({
                type: FETCH,
                payload: data
        }));
};
```

Create your `store.jsx`

```sh
import { createStore, applyMiddleware, compose } from "redux";
import reducer from "./reducers"
import thunk from "redux-thunk";

const initialState = {};
const middleware = [thunk];

const store = createStore(
    reducer,
    initialState,
    compose(
        applyMiddleware(...middleware),
    )
);

export default store;
```

In `index.jsx`, make sure to wrap high-level component with `Provider`:

```sh
ReactDOM.render(
    <Provider store={store}>
        <Test />
    </Provider>,
    document.getElementById("content")
);
```

[//]: References (http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
[full-stack web application]: <https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9>
[package.json docs]: <https://docs.npmjs.com/files/package.json>
[--save or --save-dev]: <https://imcodebased.com/npm-save-or-save-dev-which-one-to-use/>
[setting up Redux]: <https://www.youtube.com/watch?v=93p3LxR9xfM>