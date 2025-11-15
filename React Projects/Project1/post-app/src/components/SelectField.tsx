interface SelectFieldProps {
    value?: string | number;
    onChange?: (e: React.ChangeEvent<HTMLSelectElement>) => void;
    label?: string;
    error?: string;
    defaultOption?: string;
    options?: { value: string | number; label: string; id: string | number }[];
}

function SelectField(props: SelectFieldProps) {
    return (
        <div className="flex flex-col mb-4">
            {props.label && (
                <label className="mb-1 text-sm font-medium text-white">{props.label}</label>
            )}

            <select
                value={props.value ?? ""}       
                onChange={props.onChange}          
                className="border rounded-lg px-3 py-2 bg-white text-black focus:outline-none focus:ring-2 focus:ring-blue-500 border-gray-300"
            >
                <option value="">
                    {props.defaultOption || "Select an option"}
                </option>

                {props.options?.map((option) => (
                    <option key={option.id} value={option.value}>
                        {option.label}
                    </option>
                ))}
            </select>

            {props.error && (
                <p className="text-red-500 text-sm mt-1">{props.error}</p>
            )}
        </div>
    );
}

export default SelectField;
