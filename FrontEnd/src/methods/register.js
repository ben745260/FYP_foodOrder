import apiClient from '@/axios/apiClient';

const register = function (registerUser) {
    apiClient.post('/users/', {
        username: registerUser.username,
        password: registerUser.password
    })
    .then(response => {
        console.log("added registration");
        this.$router.push('/login');
    })
    .catch(error => {
        // Handle login error
        console.log(error.response.data.message);
        let response = error.response.data;
        for (let property in response) {
            if (response.hasOwnProperty(property)) {
                if (Array.isArray(response[property])) {
                    response[property].forEach(errorMsg => {
                        console.log(errorMsg);
                        // this.$toast.error(errorMsg, {
                        //     duration: 6000
                        // });
                    });
                } else {
                    console.log(errorMsg);
                    // this.$toast.error(errorMsg, {
                    //     duration: 6000
                    // });
                }
            }
        }
    });
};

export { register };