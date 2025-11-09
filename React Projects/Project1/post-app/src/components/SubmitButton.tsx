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
            className={`w-full bg-amber-100 text-slate-800 border border-lime-300 hover:bg-slate-600 hover:text-lime-300 px-4 py-2 rounded-lg text-sm font-semibold transition-all duration-200 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed`}
        >
            {loading ? "Loading..." : label}
        </button>
    );
}

export default SubmitButton;
