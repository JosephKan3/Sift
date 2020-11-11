import React from 'react'
import Youtube from '../../util/Youtube'
import './App.css';

class App extends React.Component{
    constructor(props) {
        super(props)
        this.state = {
            test: "DOG",
            // accessToken: "",
            channelName: ""
        }

    }

    async getChannelByName() {
        let response = await Youtube.getChannelByAuthorName("Pewdiepie");
        this.setState({channelName: response})
    }


    render() {
        return(
            <div>
                <h1>{this.state.channelName}</h1>
                <button onClick={this.getChannelByName}></button>
            </div>
        )
    }
}



export default App;
