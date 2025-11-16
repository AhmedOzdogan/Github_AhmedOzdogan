import { useState } from "react";
import InputField from "./InputField";
import SelectField from "./SelectField";
import useFetch from "../hooks/useFetch";

function Searchbar({ onSearch }: { onSearch: (criteria: { title: string; author: string; category: string }) => void }) {
    const { data } = useFetch<any[]>("http://localhost:8000/api/categories/");

    const [searchTitle, setSearchTitle] = useState("");
    const [searchAuthor, setSearchAuthor] = useState("");
    const [category, setCategory] = useState("");

    const handleSearch = () => {
        onSearch({
            title: searchTitle,
            author: searchAuthor,
            category: category,
        });
    }

    return (
        <div className="w-1/5 p-4 flex flex-col space-y-4 fixed left-0 top-20">
            <h2 className="text-xl font-semibold text-white">Search</h2>

            {/* Input field */}
            <InputField
                label="Author/Title"
                type="text"
                placeholder="Search title..."
                className="px-3 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-lime-500"
                value={searchTitle}
                onChange={(e: any) => setSearchTitle(e.target.value)}
            />
            <InputField
                label="Author"
                type="text"
                placeholder="Search author..."
                className="px-3 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-lime-500"
                value={searchAuthor}
                onChange={(e: any) => setSearchAuthor(e.target.value)}
            />

            {/* Category dropdown */}
            <SelectField
                defaultOption="Select a Category"
                options={
                    data
                        ? data.map((cat: any) => ({
                            value: cat.id,
                            label: cat.name,
                            id: cat.id,
                        }))
                        : []
                }
                label="Category"
                value={category}
                onChange={(e: any) => setCategory(e.target.value)}
            />

            {/* Search Button */}
            <button
                className="px-4 py-2 bg-lime-500 text-white rounded-lg hover:bg-lime-600 transition"
                onClick={handleSearch}
            >
                Search
            </button>
        </div>
    );
} 

export default Searchbar;
