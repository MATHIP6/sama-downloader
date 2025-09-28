import { useState } from "react"
import Catalogue from "../../models/catalogue";
import CatalogueList from "./CatalogueList";

export default function SearchBar() {

    const [animes, setAnimes] = useState([]);

    const search = (event: React.ChangeEvent<HTMLInputElement>) => {
        fetch('http://127.0.0.1:8000/search/' + event.target.value).then((response) => {
            response.json().then((res) => {
                const catalogues = res.map((item) => new Catalogue(item.url, item.name, item.image_url, item.genres));
                setAnimes(catalogues);
            })
        })
    }

    return (
        <div>
            <div className={`bg-stone-100 text-gray-900 dark:bg-stone-800 border-2 border-gray-400 inline-block p-2 ${(animes.length > 0) ? 'rounded-t-lg' : 'rounded-lg'} shadow-xl ring-gray-900/5 focus:border-blue-400'`}>
                <input onChange={search} type="text" placeholder="Rechercher" className="w-100 h-10"></input>
            </div>
            {animes.length > 0 && <CatalogueList catalogues={animes} />}
        </div>
    )
}
