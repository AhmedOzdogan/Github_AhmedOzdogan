interface SubmitButtonProps {
    label: string;
    onClick?: () => void;
    loading?: boolean;
    type?: "button" | "submit";
}

function SubmitButton({ label, onClick, loading, type = "submit" }: SubmitButtonProps) {
    return (
        <button
            type={type}
            onClick={onClick}
            disabled={loading}
            className={`w-full bg-blue-500 text-white py-2 rounded-lg font-medium
        hover:bg-blue-600 transition-colors duration-200
        disabled:opacity-60 disabled:cursor-not-allowed`}
        >
            {loading ? "Loading..." : label}
        </button>
    );
}

export default SubmitButton;
