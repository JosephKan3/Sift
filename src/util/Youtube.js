const axios = require('axios').default

const Youtube = {
    getChannelByAuthorName(inputchannelName) {
        console.log(inputchannelName)
        return new Promise((resolve, reject) => {
            axios.get("http://localhost:5000/channelByName", {
                channelName: inputchannelName
            })
        })
    }
}

export default Youtube;