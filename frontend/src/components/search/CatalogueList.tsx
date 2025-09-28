import type Catalogue from "../../models/catalogue";
import CatalogueComponent from "./CatalogueComponent";

export default function CatalogueList({ catalogues }) {
    return (
        <div className='z-1 shadow-xl/20 ring-gray-900/5 max-h-80 overflow-scroll'>
            {catalogues.map((catalogue) => {
                return (
                    <div>
                        <CatalogueComponent catalogue={catalogue} />
                    </div>
                )
            })}
        </div>
    )
}
