import apiClient from '@/axios/apiClient';
// import {useToast} from 'vue-toast-notification';
// import 'vue-toast-notification/dist/theme-sugar.css';

// const $toast = useToast();

const login = function (LoginUser) {
    apiClient.post('/token/login/', {
        username: LoginUser.username,
        password: LoginUser.password
    })
    .then(response => {
        const token = response.data.auth_token
        console.log(token)
        this.$store.commit('setToken', token)
        this.$router.push('/dashboard');
    })
    .catch(error => {
        // Handle login error
        let response = error.response.data;
        for (let property in response) {
            if (response.hasOwnProperty(property)) {
                if (Array.isArray(response[property])) {
                    response[property].forEach(errorMsg => {
                        $toast.error(errorMsg, {
                            duration: 6000
                        });
                    });
                } else {
                    $toast.error(errorMsg, {
                        duration: 6000
                    });
                }
            }
        }
    });
};

export { login };