const axios = require('axios').default

const Youtube = {
    getChannelByAuthorName(channelName) {
        return new Promise((resolve, reject) => {
            axios.post("http://localhost:5000/channelByName", {
                channelName: this.channelName
            })
        })
    }
}

export default Youtube;