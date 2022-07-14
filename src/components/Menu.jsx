import React from 'react'
import logo from './logo.png'
import { Link } from 'react-router-dom'

export default function Menu() {
  return (
    <div className='flex flex-col items-center'>
        <img src={logo} alt='' className=''/>
        <Link to='/goals' className='font-gilroy-bold text-[20px] pl-[27px] pt-[21px] pb-[21px] pr-[198px] mb-[34px] bg-main text-white rounded-[10px]'>Цели</Link>
        <Link to='/goals' className='font-gilroy-bold text-[20px] pl-[20px] pt-[21px] pb-[21px] pr-[190px] mb-[34px] text-[#797C85] rounded-[10px] hover: bg-main text-white'>Мечты</Link>
        <Link to='/goals' className='font-gilroy-bold text-[20px] pl-[18px] pt-[21px] pb-[21px] pr-[185px] mb-[34px] text-[#797C85] rounded-[10px]'>Задачи</Link>
        <Link to='/goals' className='font-gilroy-bold text-[20px] pl-[16px] pt-[21px] pb-[21px] pr-[180px] mb-[34px] text-[#797C85] rounded-[10px]'>Заметки</Link>
        <Link to='/goals' className='font-gilroy-bold text-[20px] pl-[20px] pt-[21px] pb-[21px] pr-[190px] mb-[34px] text-[#797C85] rounded-[10px]'>Статьи</Link>
    </div>
  )
}
