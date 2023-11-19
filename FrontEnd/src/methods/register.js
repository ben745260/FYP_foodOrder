import apiClient from '@/axios/apiClient';
// import {useToast} from 'vue-toast-notification';
// import 'vue-toast-notification/dist/theme-sugar.css';

// const $toast = useToast();

const register = function (registerUser) {
    apiClient.post('/users/', {
        username: registerUser.username,
        password: registerUser.password
    })
    .then(response => {
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
                        $toast.error(errorMsg, {
                            duration: 6000
                        });
                    });
                } else {
                    console.log(errorMsg);
                    $toast.error(errorMsg, {
                        duration: 6000
                    });
                }
            }
        }
    });
};

export { register };