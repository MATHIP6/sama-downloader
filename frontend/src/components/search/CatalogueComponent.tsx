import type Catalogue from "../../models/catalogue";

const formatGenres = (genres: string[]) => {
    const limitedGenres = genres.slice(0, 3);
    const formatted = limitedGenres.join(', ');
    return genres.length > 3 ? `${formatted}...` : formatted;
}

function CatalogueComponent({ catalogue }: { catalogue: Catalogue }) {
    return (
        <div className="flex flex-row w-105 h-15 border-2 border-gray-400">
            <img src={catalogue.image_url} width={100} alt={`${catalogue.name} cover`} className="m-1 rounded-lg" />
            <div>
                <p className="grow ml-5 font-semibold text-sm">{catalogue.name}</p>
                <i className="text-gray-700 text-sm">{formatGenres(catalogue.genres)}</i>
            </div>
        </div>
    )
}

export default CatalogueComponent;
