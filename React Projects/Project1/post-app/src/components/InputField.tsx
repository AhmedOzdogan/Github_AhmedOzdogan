import React from "react";

interface InputFieldProps {
    type?: string;
    placeholder?: string;
    label?: string;
    value?: string;
    onChange?: (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void;
    error?: string;
    height?: number;              // custom height in px
    fullWidth?: boolean;          // stretch to full width
    size?: "sm" | "md" | "lg";    // font & padding size
    textarea?: boolean;           // switch to textarea mode
    className?: string;           // custom override
}

function InputField({
    type = "text",
    placeholder,
    label,
    value,
    onChange,
    error,
    height,
    fullWidth = true,
    size = "md",
    textarea = false,
    className = "",
}: InputFieldProps) {
    const sizeClasses = {
        sm: "text-sm px-2 py-1",
        md: "text-base px-3 py-2",
        lg: "text-lg px-4 py-3",
    };

    const baseClasses =
        `border rounded-lg focus:outline-none focus:ring-2 
        ${error ? "border-red-500 focus:ring-red-400" : "border-gray-300 focus:ring-blue-500"}
        ${sizeClasses[size]}
        ${fullWidth ? "w-full" : ""}
        bg-white text-black
        ${className}`;

    return (
        <div className="flex flex-col mb-4">
            {label && (
                <label className="mb-1 text-sm font-medium text-white">{label}</label>
            )}

            {textarea ? (
                <textarea
                    placeholder={placeholder}
                    value={value}
                    onChange={onChange}
                    className={baseClasses}
                    style={height ? { height: `${height}px` } : undefined}
                />
            ) : (
                <input
                    type={type}
                    placeholder={placeholder}
                    value={value}
                    onChange={onChange}
                    className={baseClasses}
                    style={height ? { height: `${height}px` } : undefined}
                />
            )}

            {error && <p className="text-red-500 text-xs mt-1">{error}</p>}
        </div>
    );
}

export default InputField;
