import React, { useState } from 'react'
import axios from 'axios';
import validator from 'validator';

const DOMEN_SERVER = '';
const DOMEN_SITE = '';

export default function SignUp() {

    const [register, setRegister] = useState(() => {
        return {
            email: "",
            password: "",
        }
    })
     
    const changeInputRegister = event => {
        event.persist()
        setRegister(prev => {
            return {
                ...prev,
                [event.target.name]: event.target.value,
            }
        })
    }

    const submitChackin = event => {
        event.preventDefault();
        if(!validator.isEmail(register.email)) {
            alert("You did not enter email")
        } else if(!validator.isStrongPassword(register.password, {minSymbols: 0})) {
            alert("Password must consist of one lowercase, uppercase letter and number, at least 8 characters")
        } else {
            axios.post(DOMEN_SERVER + "/auth/registration/", {
                username: register.username,
                email: register.email,
                password: register.password,
            }).then(res => {
                if (res.data === true) {
                    window.location.href = DOMEN_SITE + "/auth"
                } else {
                    alert("There is already a user with this email")
                }
            }).catch(() => {
                alert("An error occurred on the server")
            })
        }
    }

  return (
    <div className="text-center mt-[130px]">
        <h2 className='font-gilroy-bold text-[50px]'>Вход в аккаунт</h2>
        <h3 className='font-gilroy-bold text-[16px]'>Нет аккаунта? <a href='' className='underline text-main'>зарегистрироваться</a></h3>
        <form onSubmit={submitChackin} >
            <div className="flex flex-col text-center ml-[490px]">
            <input
            className="font-gilroy-medium text-[18px] mt-[10px] pl-[29px] pt-[22px] pb-[22px] bg-[#F6F8FF] w-[50%] rounded-[15px]"
            type="email"
            id="email"
            name="email"
            placeholder="Email"
            value={register.email}
            onChange={changeInputRegister}
            formnovalidate
            />
            <input
            className="font-gilroy-medium text-[18px] mt-[10px] outline-1 pl-[29px] pt-[22px] pb-[22px] bg-[#F6F8FF] w-[50%] rounded-[15px]"
            type="password"
            id="password"
            name="password"
            placeholder="Пароль"
            value={register.password}
            onChange={changeInputRegister}
            /></div>
            <input type="submit" className='mt-[30px] font-gilroy-bold text-[20px] text-white pl-[140px] pr-[140px] py-[21px] bg-main rounded-[15px] ml-[15px]' value="Войти в аккаунт"/>
        </form>
    </div>
  )
}

