import Header from './components/Header'
import SearchBar from './components/search/SearchBar'
import './index.css'

export default function Home() {
    return (
        <div className='bg-white dark:bg-gray-950 m-0 dark:text-blue-50 w-full h-full'>
            <Header />
            <div className='flex justify-center m-32'>
                <SearchBar />
            </div>
        </div>)
}
