import React from "react";

// InputField component props interface
interface InputFieldProps {
    type: string;
    placeholder?: string;
    label?: string;
    value?: string;
    onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
    error?: string;
}

// InputField component definition
function InputField({
    type,
    placeholder,
    label,
    value,
    onChange,
    error,
}: InputFieldProps) {
    return (
        <div className="flex flex-col mb-4">
            {label && (
                <label className="mb-1 text-sm font-medium text-gray-700">{label}</label>
            )}
            <input
                type={type}
                placeholder={placeholder}
                value={value}
                onChange={onChange}
                className={`border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 ${error ? "border-red-500" : "border-gray-300"
                    }`}
            />
            {error && <p className="text-red-500 text-xs mt-1">{error}</p>}
        </div>
    );
}

export default InputField;
