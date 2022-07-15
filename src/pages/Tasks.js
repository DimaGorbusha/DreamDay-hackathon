import React from 'react'
import logo from './logo.png'
import tasks from './tasks.png'
import { Link } from 'react-router-dom'

export default function Tasks() {
  return (
    <div className="flex mt-[91px]">
      <div className='flex flex-col items-center ml-[99px]'>
        <img src={logo} alt='' className=''/>
        <Link to='/' className='font-gilroy-bold text-[20px] pl-[27px] pt-[21px] pb-[21px] pr-[198px] mb-[34px] mt-[58px] text-[#797C85] rounded-[10px] hover:text-white hover:bg-main transition delay-75 ease-in-out'>Цели</Link>
        <Link to='/dreams' className='font-gilroy-bold text-[20px] pl-[20px] pt-[21px] pb-[21px] pr-[190px] mb-[34px] text-[#797C85] rounded-[10px] hover:text-white hover:bg-main transition delay-75 ease-in-out'>Мечты</Link>
        <Link to='/tasks' className='font-gilroy-bold text-[20px] pl-[18px] pt-[21px] pb-[21px] pr-[185px] mb-[34px] bg-main text-white rounded-[10px]'>Задачи</Link>
        <Link to='/notes' className='font-gilroy-bold text-[20px] pl-[16px] pt-[21px] pb-[21px] pr-[180px] mb-[34px] text-[#797C85] rounded-[10px] hover:text-white hover:bg-main transition delay-75 ease-in-out'>Заметки</Link>
        <Link to='/articles' className='font-gilroy-bold text-[20px] pl-[20px] pt-[21px] pb-[21px] pr-[190px] mb-[34px] text-[#797C85] rounded-[10px] hover:text-white hover:bg-main transition delay-75 ease-in-out'>Статьи</Link>
      </div>
      <div>
        <img src={tasks} alt='' className='ml-[35px]' />
      </div>
    </div>
  )
}