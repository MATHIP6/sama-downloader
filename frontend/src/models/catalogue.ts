class Catalogue {

    public url: string;
    public name: string;
    public image_url: string;
    public genres: string[];

    constructor(url: string, name: string, image_url: string, genres: string[]) {
        this.url = url;
        this.name = name;
        this.image_url = image_url;
        this.genres = genres;
    }
}

export default Catalogue;
