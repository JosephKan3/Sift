const axios = require('axios').default


const Youtube = {
    getChannelByAuthorName(inputchannelName) {
        console.log(inputchannelName)
        return new Promise((resolve, reject) => {
            // axios.post("localhost:5000/channelByName", {
            //     channelName: "Pewdiepie"
            // })
            // axios({
            //     method: 'post',
            //     url: 'http://localhost:5000/channelByName',
            //     data: {
            //         channelName: inputchannelName
            //     }
            // });
            // fetch("https://localhost:5000/channelByName", {
            //     headers: {
            //         "content-type": "application/json",
            //     },
            //     method: "POST",
            //     body: JSON.stringify({channelName: inputchannelName})
            // })
            fetch(`http://localhost:5000/channelByName/${inputchannelName}`)
        })
    }
}

export default Youtube;