interface FormContainerProps {
    title?: string;
    children?: React.ReactNode;
}

function FormContainer({ title, children }: FormContainerProps) {
    return (
        <div className="flex justify-center items-start mt-14 min-h-screen bg-slate-800">
            <div className="bg-slate-600 shadow-md rounded-xl p-8 w-full min-w-100 max-w-md">
                {title && (
                    <h2 className="text-2xl font-semibold text-center mb-6 text-white">
                        {title}
                    </h2>
                )}
                {children}
            </div>
        </div>
    );
}

export default FormContainer;
