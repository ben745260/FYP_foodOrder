import apiClient from '@/axios/apiClient';

const login = function (LoginUser) {
    apiClient.post('/token/login/', {
        username: LoginUser.username,
        password: LoginUser.password
    })
    .then(response => {
        console.log("logined");
        const token = response.data.auth_token
        console.log(token);

        this.$router.push('/dashboard');
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

export { login };